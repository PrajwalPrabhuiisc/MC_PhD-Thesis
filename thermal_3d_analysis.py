import numpy as np
import open3d as o3d
from scipy import stats
from preprocess import extract_thermal_frames, normalize_thermal_data, save_processed_frames
from visualize import visualize_point_cloud

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

# Generate a synthetic 3D point cloud
def generate_point_cloud():
    # Since no point cloud file is available, generate a synthetic cube
    print("Generating synthetic point cloud (cube shape)...")
    points = []
    for x in np.linspace(-1, 1, 50):
        for y in np.linspace(-1, 1, 50):
            for z in np.linspace(-1, 1, 50):
                points.append([x, y, z])
    points = np.array(points)
    
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    
    # Placeholder for loading a real point cloud in the future
    # If you have a point cloud file (e.g., 'data/point_cloud.ply'), you can load it instead:
    # pcd = o3d.io.read_point_cloud("data/point_cloud.ply")
    # points = np.asarray(pcd.points)
    
    return pcd, points

# Map thermal anomalies to 3D point cloud
def map_anomalies_to_3d(points, anomalies, frames):
    colors = np.zeros((points.shape[0], 3))
    anomaly_frame = anomalies[0]  # Use first frame for simplicity
    frame_h, frame_w = anomaly_frame.shape
    
    for i, point in enumerate(points):
        x, y, _ = point
        u = int((x + 1) / 2 * frame_w)
        v = int((y + 1) / 2 * frame_h)
        
        if 0 <= u < frame_w and 0 <= v < frame_h:
            if anomaly_frame[v, u] > 0:
                colors[i] = [1, 0, 0]  # Red for anomalies
            else:
                colors[i] = [0, 0, 1]  # Blue for normal
    
    return colors

# Main pipeline
def main():
    video_path = "data/thermal_video.mp4"
    
    try:
        # Preprocess video
        print("Extracting and normalizing thermal frames...")
        frames = extract_thermal_frames(video_path)
        normalized_frames = normalize_thermal_data(frames)
        save_processed_frames(normalized_frames)
        
        # Detect anomalies
        print("Detecting thermal anomalies...")
        anomalies = detect_thermal_anomalies(normalized_frames)
        
        # Generate point cloud
        print("Generating 3D point cloud...")
        pcd, points = generate_point_cloud()
        
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
