import numpy as np
import open3d as o3d
from scipy import stats
from subprocess import run
from preprocess import extract_thermal_frames, enhance_thermal_frames, normalize_thermal_data, save_processed_frames, save_frames_for_odm
from visualize import visualize_point_cloud
import os

# Statistical anomaly detection
def detect_thermal_anomalies(frames):
    all_temperatures = frames.flatten()
    z_scores = np.abs(stats.zscore(all_temperatures))
    threshold = 2.5
    anomalies = np.zeros_like(frames, dtype=np.uint8)
    
    for i in range(frames.shape[0]):
        frame = frames[i]
        z_frame = np.abs(stats.zscore(frame.flatten())).reshape(frame.shape)
        anomalies[i] = (z_frame > threshold).astype(np.uint8) * 255
    
    return anomalies

# Generate point cloud using OpenDroneMap from thermal frames
def generate_point_cloud(image_dir="data/images/", output_path="output/point_cloud.ply"):
    print("Generating point cloud with OpenDroneMap...")
    os.makedirs("output", exist_ok=True)
    
    # Run ODM via Docker
    run([
        "docker", "run", "-ti", "--rm",
        "-v", f"{os.path.abspath(image_dir)}:/code/images",
        "-v", f"{os.path.abspath('output')}:/code/odm_output",
        "opendronemap/odm",
        "--project-path", "/code/odm_output",
        "--images", "/code/images",
        "--pc-quality", "medium",  # Adjust for better results with thermal data
        "--feature-type", "sift"   # SIFT may work better for grayscale thermal images
    ], check=True)
    
    # ODM typically outputs to 'odm_output/odm_georeferenced_model.ply'
    odm_output_path = "output/odm_georeferenced_model.ply"
    if not os.path.exists(odm_output_path):
        raise FileNotFoundError("ODM failed to generate point cloud.")
    
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(odm_output_path)
    if not pcd.has_points():
        raise ValueError("Loaded point cloud is empty.")
    points = np.asarray(pcd.points)
    
    # Save to specified output path for consistency
    o3d.io.write_point_cloud(output_path, pcd)
    return pcd, points

# Map thermal anomalies to 3D point cloud
def map_anomalies_to_3d(points, anomalies, frames):
    colors = np.zeros((points.shape[0], 3))
    anomaly_frame = anomalies[0]  # Use first frame for simplicity
    frame_h, frame_w = anomaly_frame.shape
    
    # Scale points to match frame dimensions (assuming top-down alignment)
    x_min, x_max = points[:, 0].min(), points[:, 0].max()
    y_min, y_max = points[:, 1].min(), points[:, 1].max()
    
    for i, point in enumerate(points):
        x, y, _ = point
        u = int(((x - x_min) / (x_max - x_min)) * frame_w)
        v = int(((y - y_min) / (y_max - y_min)) * frame_h)
        
        if 0 <= u < frame_w and 0 <= v < frame_h:
            if anomaly_frame[v, u] > 0:
                colors[i] = [1, 0, 0]  # Red for anomalies
            else:
                colors[i] = [0, 0, 1]  # Blue for normal
    
    return colors

# Main pipeline
def main():
    video_path = "data/thermal_video.mp4"
    image_dir = "data/images/"
    
    try:
        # Preprocess video and prepare frames for ODM
        print("Extracting thermal frames...")
        frames = extract_thermal_frames(video_path)
        print("Enhancing frames for ODM...")
        enhanced_frames = enhance_thermal_frames(frames)
        print("Saving frames for ODM...")
        save_frames_for_odm(enhanced_frames, image_dir)
        
        # Normalize frames for anomaly detection
        print("Normalizing thermal frames...")
        normalized_frames = normalize_thermal_data(frames)
        save_processed_frames(normalized_frames)
        
        # Detect anomalies
        print("Detecting thermal anomalies...")
        anomalies = detect_thermal_anomalies(normalized_frames)
        
        # Generate point cloud with ODM
        print("Generating 3D point cloud with OpenDroneMap...")
        pcd, points = generate_point_cloud(image_dir)
        
        # Map anomalies to 3D
        print("Mapping anomalies to 3D point cloud...")
        colors = map_anomalies_to_3d(points, anomalies, normalized_frames)
        
        # Visualize
        print("Visualizing...")
        visualize_point_cloud(pcd, colors)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
