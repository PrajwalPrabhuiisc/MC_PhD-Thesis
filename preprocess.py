import cv2
import numpy as np
import os

def extract_thermal_frames(video_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
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
    
    if not frames:
        raise ValueError("No frames extracted from the video.")
    
    return np.array(frames)

def normalize_thermal_data(frames):
    # Normalize thermal data to [0, 1] for consistency
    min_val, max_val = frames.min(), frames.max()
    if max_val == min_val:
        raise ValueError("Thermal data has no variation (min == max).")
    normalized_frames = (frames - min_val) / (max_val - min_val)
    return (normalized_frames * 255).astype(np.uint8)

def save_processed_frames(frames, output_dir="output/"):
    os.makedirs(output_dir, exist_ok=True)
    for i, frame in enumerate(frames):
        cv2.imwrite(f"{output_dir}/frame_{i}.png", frame)
    print(f"Saved {len(frames)} processed frames to {output_dir}")
