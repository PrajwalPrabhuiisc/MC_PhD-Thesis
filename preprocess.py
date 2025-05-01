import cv2
import numpy as np

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

def normalize_thermal_data(frames):
    # Normalize thermal data to [0, 1] for consistency
    normalized_frames = (frames - frames.min()) / (frames.max() - frames.min())
    return (normalized_frames * 255).astype(np.uint8)

def save_processed_frames(frames, output_dir="output/"):
    for i, frame in enumerate(frames):
        cv2.imwrite(f"{output_dir}frame_{i}.png", frame)
