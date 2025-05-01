import cv2
import numpy as np
import open3d as o3d
from scipy import stats

# Step 1: Load and preprocess thermal video
def extract_thermal_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Convert to grayscale (assuming thermal data is in intensity)
        thermal_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(thermal_frame)
    cap.release()
    return np.array(frames)

# Step 2: Statistical anomaly detection
def detect_thermal_anomalies(frames):
    # Flatten frames to 1D for statistical analysis
    all_temperatures = frames.flatten()
    
    # Use z-score for anomaly detection
    z_scores = np.abs(stats.zscore(all_temperatures))
    threshold = 2.5  # Z-score threshold for anomalies
    anomalies = np.zeros_like(frames, dtype=np.uint8)
    
    for i in range(frames.shape[0]):
        frame = frames[i]
        z_frame = np.abs(stats.zscore(frame.flatten())).reshape(frame.shape)
        anomalies[i] = (z_frame > threshold).astype(np.uint8) * 255
    
    return anomalies

# Step 3: Generate a synthetic 3D point cloud (simulating prefab module)
def generate_point_cloud():
    # Create a simple cube as a placeholder for the prefab module
    points = []
    for x in np.linspace(-1, 1, 50):
        for y in np.linspace(-1, 1, 50):
            for z in np.linspace(-1, 1, 50):
                points.append([x, y, z])
    points = np.array(points)
    
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd, points

# Step 4: Map thermal anomalies to 3D point cloud
def map_anomalies_to_3d(points, anomalies, frames):
    # Simplified mapping: Assume anomalies align with the XY plane at z=0
    colors = np.zeros((points.shape[0], 3))  # RGB colors for point cloud
    
    # Map 2D anomaly pixels to 3D points (simplified projection)
    anomaly_frame = anomalies[0]  # Use first frame for simplicity
    frame_h, frame_w = anomaly_frame.shape
    
    for i, point in enumerate(points):
        x, y, _ = point
        # Map 3D coordinates to 2D image coordinates
        u = int((x + 1) / 2 * frame_w)  # Scale [-1, 1] to [0, frame_w]
        v = int((y + 1) / 2 * frame_h)  # Scale [-1, 1] to [0, frame_h]
        
        if 0 <= u < frame_w and 0 <= v < frame_h:
            if anomaly_frame[v, u] > 0:
                colors[i] = [1, 0, 0]  # Red for anomalies
            else:
                colors[i] = [0, 0, 1]  # Blue for normal
    
    return colors

# Step 5: Visualize the 3D point cloud with anomalies
def visualize_point_cloud(pcd, colors):
    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd])

# Main pipeline
def main():
    # Paths and parameters
    video_path = "thermal_video.mp4"
    
    # Extract frames
    print("Extracting thermal frames...")
    frames = extract_thermal_frames(video_path)
    
    # Detect anomalies
    print("Detecting thermal anomalies...")
    anomalies = detect_thermal_anomalies(frames)
    
    # Generate point cloud
    print("Generating 3D point cloud...")
    pcd, points = generate_point_cloud()
    
    # Map anomalies to 3D
    print("Mapping anomalies to 3D point cloud...")
    colors = map_anomalies_to_3d(points, anomalies, frames)
    
    # Visualize
    print("Visualizing...")
    visualize_point_cloud(pcd, colors)

if __name__ == "__main__":
    main()
