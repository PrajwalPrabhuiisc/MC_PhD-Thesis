import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from pywt import wavedec
import tensorflow as tf
from tensorflow.keras import layers, Model, callbacks

# --- Setup Output Directories ---
output_dir = 'anomaly_detection_results'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
visualizations_dir = os.path.join(output_dir, 'visualizations')
if not os.path.exists(visualizations_dir):
    os.makedirs(visualizations_dir)

# --- Data Parsing Functions ---
def parse_line(line):
    timestamp_match = re.match(r"([\d:.]+)\s*->", line)
    timestamp = timestamp_match.group(1) if timestamp_match else None
    sensor_pattern = r"Sensor\s+(\d+)\s+-\s+X:\s+([-0-9.]+)\s+Y:\s+([-0-9.]+)\s+Z:\s+([-0-9.]+)"
    matches = re.findall(sensor_pattern, line)
    data = {"timestamp": timestamp}
    for sensor_num, x, y, z in matches:
        data[f"sensor{sensor_num}_X"] = float(x)
        data[f"sensor{sensor_num}_Y"] = float(y)
        data[f"sensor{sensor_num}_Z"] = float(z)
    return data

def load_data_from_directory(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        line = line.strip()
                        if line:
                            parsed_data = parse_line(line)
                            data_list.append(parsed_data)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    if not data_list:
        raise ValueError(f"No valid data found in directory '{directory}'.")
    return pd.DataFrame(data_list)

# --- Feature Engineering ---
def compute_magnitude(df, sensor_num):
    x = df[f"sensor{sensor_num}_X"]
    y = df[f"sensor{sensor_num}_Y"]
    z = df[f"sensor{sensor_num}_Z"]
    return np.sqrt(x**2 + y**2 + z**2)

def multi_res_features(data, level=1):
    coeffs = wavedec(data, 'db1', level=level)
    return np.concatenate(coeffs)

def compute_features(df):
    for sensor in range(1, 5):
        df[f"sensor{sensor}_mag"] = compute_magnitude(df, sensor)
    mag_cols = [f"sensor{s}_mag" for s in range(1, 5)]
    multi_res_scaler = StandardScaler()
    pca = PCA(n_components=5)
    for col in mag_cols:
        multi_res = np.array([multi_res_features(df[col].values[i:i+16])
                              for i in range(0, len(df) - 15)])
        multi_res_scaled = multi_res_scaler.fit_transform(multi_res)
        multi_res_reduced = pca.fit_transform(multi_res_scaled)
        df = df.iloc[15:]
        df.loc[:, f"{col}_multi_res"] = list(multi_res_reduced)
    df["s1_s2_ratio"] = df["sensor1_mag"] / (df["sensor2_mag"] + 1e-6)
    df["s3_s4_ratio"] = df["sensor3_mag"] / (df["sensor4_mag"] + 1e-6)
    df["mean_mag"] = df[mag_cols].mean(axis=1)
    df["std_mag"] = df[mag_cols].std(axis=1)
    df["max_mag"] = df[mag_cols].max(axis=1)
    return df

# --- Dense Autoencoder ---
def build_autoencoder(input_dim, encoding_dim=16, intermediate_dims=[64, 32]):
    inputs = layers.Input(shape=(input_dim,))
    # Encoder
    x = inputs
    for dim in intermediate_dims:
        x = layers.Dense(dim, activation='relu')(x)
        x = layers.Dropout(0.2)(x)
    encoded = layers.Dense(encoding_dim, activation='relu')(x)
    # Decoder
    x = encoded
    for dim in reversed(intermediate_dims):
        x = layers.Dense(dim, activation='relu')(x)
        x = layers.Dropout(0.2)(x)
    outputs = layers.Dense(input_dim)(x)
    autoencoder = Model(inputs, outputs, name='autoencoder')
    encoder = Model(inputs, encoded, name='encoder')

    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate=0.0001, decay_steps=10000, decay_rate=0.9
    )
    optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)
    autoencoder.compile(optimizer=optimizer, loss='mae')
    return autoencoder, encoder

# --- Estimate Epistemic Uncertainty with Monte Carlo Dropout ---
def estimate_epistemic_uncertainty(model, X, num_samples=50):
    # Enable dropout during inference
    model.trainable = False
    reconstructions = []
    for _ in range(num_samples):
        recon = model(X, training=True)  # training=True ensures dropout is active
        reconstructions.append(recon.numpy())
    reconstructions = np.array(reconstructions)  # Shape: (num_samples, n_samples, input_dim)
    epistemic_variance = np.var(reconstructions, axis=0)  # Variance across MC samples
    epistemic_uncertainty = np.mean(epistemic_variance, axis=1)  # Mean variance per sample
    return epistemic_uncertainty

# --- Main Pipeline ---
train_dir = '/content/Train'
test_dir = '/content/Test'

df_train = load_data_from_directory(train_dir)
df_test = load_data_from_directory(test_dir)

df_train = compute_features(df_train)
df_test = compute_features(df_test)

feature_cols = [f"sensor{s}_mag" for s in range(1, 5)] + \
               [f"sensor{s}_mag_multi_res" for s in range(1, 5)] + \
               ["s1_s2_ratio", "s3_s4_ratio", "mean_mag", "std_mag", "max_mag"]

X_train = np.array([np.concatenate([df_train[col].iloc[i] if 'multi_res' in col else [df_train[col].iloc[i]]
                                   for col in feature_cols]) for i in range(len(df_train))])
X_test = np.array([np.concatenate([df_test[col].iloc[i] if 'multi_res' in col else [df_test[col].iloc[i]]
                                  for col in feature_cols]) for i in range(len(df_test))])

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_scaled = np.nan_to_num(X_train_scaled, nan=0.0, posinf=1e6, neginf=-1e6)
X_test_scaled = np.nan_to_num(X_test_scaled, nan=0.0, posinf=1e6, neginf=-1e6)

# --- Ensemble Anomaly Detection ---
iso_forest = IsolationForest(contamination=0.1, random_state=42, n_estimators=200)
iso_forest.fit(X_train_scaled)
train_anomaly_labels_if = iso_forest.predict(X_train_scaled)
test_anomaly_labels_if = iso_forest.predict(X_test_scaled)
train_anomaly_scores_if = -iso_forest.decision_function(X_train_scaled)
test_anomaly_scores_if = -iso_forest.decision_function(X_test_scaled)

gmm = GaussianMixture(n_components=2, covariance_type='full', random_state=42)
gmm.fit(X_train_scaled)
train_anomaly_scores_gmm = -gmm.score_samples(X_train_scaled)
test_anomaly_scores_gmm = -gmm.score_samples(X_test_scaled)

input_dim = X_train_scaled.shape[1]
autoencoder, encoder = build_autoencoder(input_dim)
early_stopping = callbacks.EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)
history = autoencoder.fit(X_train_scaled, X_train_scaled, epochs=300, batch_size=64, verbose=1,
                         validation_split=0.1, callbacks=[early_stopping])

# Save training history plot
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss (MAE)')
plt.title('Autoencoder Training History')
plt.legend()
plt.savefig(os.path.join(visualizations_dir, 'training_history.png'))
plt.show()

# Compute reconstruction errors and uncertainties
train_recon = autoencoder.predict(X_train_scaled)
test_recon = autoencoder.predict(X_test_scaled)
train_anomaly_scores_ae = np.mean(np.abs(X_train_scaled - train_recon), axis=1)
test_anomaly_scores_ae = np.mean(np.abs(X_test_scaled - test_recon), axis=1)

# Estimate epistemic uncertainty using Monte Carlo Dropout
train_epistemic_uncertainty = estimate_epistemic_uncertainty(autoencoder, X_train_scaled)
test_epistemic_uncertainty = estimate_epistemic_uncertainty(autoencoder, X_test_scaled)

# Estimate aleatoric uncertainty as the variance of reconstruction errors across features
train_aleatoric_uncertainty = np.var(np.abs(X_train_scaled - train_recon), axis=1)
test_aleatoric_uncertainty = np.var(np.abs(X_test_scaled - test_recon), axis=1)

# Debug reconstruction with uncertainty
with open(os.path.join(output_dir, 'reconstruction_debug_with_uncertainty.txt'), 'w') as f:
    for i in range(5):
        debug_str = f"Sample {i}:\n"
        debug_str += f"Original: {X_train_scaled[i][:5]}\n"
        debug_str += f"Reconstructed: {train_recon[i][:5]}\n"
        debug_str += f"MAE: {train_anomaly_scores_ae[i]:.6f}\n"
        debug_str += f"Epistemic Uncertainty: {train_epistemic_uncertainty[i]:.6f}\n"
        debug_str += f"Aleatoric Uncertainty: {train_aleatoric_uncertainty[i]:.6f}\n\n"
        print(debug_str)
        f.write(debug_str)

# Normalize scores
def normalize_scores(scores):
    return (scores - scores.min()) / (scores.max() - scores.min() + 1e-6)

train_anomaly_scores_if_norm = normalize_scores(train_anomaly_scores_if)
test_anomaly_scores_if_norm = normalize_scores(test_anomaly_scores_if)
train_anomaly_scores_gmm_norm = normalize_scores(train_anomaly_scores_gmm)
test_anomaly_scores_gmm_norm = normalize_scores(test_anomaly_scores_gmm)
train_anomaly_scores_ae_norm = normalize_scores(train_anomaly_scores_ae)
test_anomaly_scores_ae_norm = normalize_scores(test_anomaly_scores_ae)

ensemble_weights = [0.4, 0.3, 0.3]
train_ensemble_scores = (ensemble_weights[0] * train_anomaly_scores_if_norm +
                         ensemble_weights[1] * train_anomaly_scores_gmm_norm +
                         ensemble_weights[2] * train_anomaly_scores_ae_norm)
test_ensemble_scores = (ensemble_weights[0] * test_anomaly_scores_if_norm +
                        ensemble_weights[1] * test_anomaly_scores_gmm_norm +
                        ensemble_weights[2] * test_anomaly_scores_ae_norm)

# --- Adaptive Assessment ---
uncertainty_threshold = np.percentile(test_anomaly_scores_ae, 90)
results = pd.DataFrame({
    "Timestamp": df_test["timestamp"],
    "IF_Anomaly_Label": test_anomaly_labels_if,
    "Ensemble_Anomaly_Score": test_ensemble_scores,
    "AE_Reconstruction_Error": test_anomaly_scores_ae,
    "Epistemic_Uncertainty": test_epistemic_uncertainty,
    "Aleatoric_Uncertainty": test_aleatoric_uncertainty,
    "Flag_for_Review": test_anomaly_scores_ae > uncertainty_threshold
})
print("\nAdaptive Assessment Results (Test Set):")
print(results.head(10))
print(f"Flagged for Review: {results['Flag_for_Review'].sum()} samples ({results['Flag_for_Review'].mean()*100:.2f}%)")

# Save results to CSV
results.to_csv(os.path.join(output_dir, 'adaptive_assessment_results.csv'), index=False)

# --- Visualization with Uncertainty ---
# Ensemble Anomaly Score vs. Reconstruction Error with Epistemic Uncertainty
plt.figure(figsize=(10, 6))
plt.errorbar(test_ensemble_scores, test_anomaly_scores_ae, yerr=test_epistemic_uncertainty, fmt='o', alpha=0.5, label='Epistemic Uncertainty', color='blue')
plt.scatter(test_ensemble_scores, test_anomaly_scores_ae, c=test_anomaly_labels_if, cmap='coolwarm', alpha=0.5)
plt.xlabel('Ensemble Anomaly Score')
plt.ylabel('Reconstruction Error (AE)')
plt.title('Ensemble Anomaly Score vs. Reconstruction Error with Epistemic Uncertainty (Test Set)')
plt.colorbar(label='Isolation Forest Anomaly Label')
plt.legend()
plt.savefig(os.path.join(visualizations_dir, 'ensemble_vs_reconstruction_with_epistemic.png'))
plt.show()

# Test Data in PCA Space with Aleatoric Uncertainty
pca = PCA(n_components=2)
X_test_pca = pca.fit_transform(X_test_scaled)
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=test_ensemble_scores, cmap='coolwarm', alpha=0.5, s=test_aleatoric_uncertainty*1e5)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Test Data in PCA Space with Aleatoric Uncertainty (Size Proportional to Uncertainty)')
plt.colorbar(label='Ensemble Anomaly Score')
plt.savefig(os.path.join(visualizations_dir, 'pca_space_with_aleatoric.png'))
plt.show()

# Multi-Resolution Wavelet Coefficients
plt.figure(figsize=(10, 6))
multi_res_example = df_test["sensor1_mag_multi_res"].iloc[0]
plt.plot(multi_res_example, label='Wavelet Coefficients', color='blue')
plt.xlabel('Coefficient Index')
plt.ylabel('Value')
plt.title('Multi-Resolution Wavelet Coefficients (Sensor 1, Sample 1)')
plt.legend()
plt.savefig(os.path.join(visualizations_dir, 'wavelet_coefficients.png'))
plt.show()

# Ensemble Anomaly Score: Flagged vs. Not Flagged
plt.figure(figsize=(10, 6))
plt.hist(test_ensemble_scores[results["Flag_for_Review"] == False], bins=50, alpha=0.7, label='Not Flagged', color='green')
plt.hist(test_ensemble_scores[results["Flag_for_Review"] == True], bins=50, alpha=0.7, label='Flagged', color='red')
plt.xlabel('Ensemble Anomaly Score')
plt.ylabel('Frequency')
plt.title('Ensemble Anomaly Score: Flagged vs. Not Flagged')
plt.legend()
plt.savefig(os.path.join(visualizations_dir, 'ensemble_histogram.png'))
plt.show()

# --- Model Performance Evaluation ---
def evaluate_model_performance(train_scores_ae, test_scores_ae, test_ensemble_scores, results, train_epistemic, test_epistemic, train_aleatoric, test_aleatoric):
    print("\n=== Model Performance Evaluation ===")

    # Reconstruction Error Statistics
    train_recon_mean = np.mean(train_scores_ae)
    train_recon_std = np.std(train_scores_ae)
    test_recon_mean = np.mean(test_scores_ae)
    test_recon_std = np.std(test_scores_ae)
    print("Reconstruction Error (MAE) Statistics:")
    print(f"Training - Mean: {train_recon_mean:.6f}, Std: {train_recon_std:.6f}")
    print(f"Test - Mean: {test_recon_mean:.6f}, Std: {test_recon_std:.6f}")

    # Uncertainty Statistics
    train_epistemic_mean = np.mean(train_epistemic)
    train_epistemic_std = np.std(train_epistemic)
    test_epistemic_mean = np.mean(test_epistemic)
    test_epistemic_std = np.std(test_epistemic)
    train_aleatoric_mean = np.mean(train_aleatoric)
    train_aleatoric_std = np.std(train_aleatoric)
    test_aleatoric_mean = np.mean(test_aleatoric)
    test_aleatoric_std = np.std(test_aleatoric)
    print("\nEpistemic Uncertainty Statistics:")
    print(f"Training - Mean: {train_epistemic_mean:.6f}, Std: {train_epistemic_std:.6f}")
    print(f"Test - Mean: {test_epistemic_mean:.6f}, Std: {test_epistemic_std:.6f}")
    print("\nAleatoric Uncertainty Statistics:")
    print(f"Training - Mean: {train_aleatoric_mean:.6f}, Std: {train_aleatoric_std:.6f}")
    print(f"Test - Mean: {test_aleatoric_mean:.6f}, Std: {test_aleatoric_std:.6f}")

    # Flagged Percentage
    flagged_percentage = results['Flag_for_Review'].mean() * 100
    print(f"\nFlagged Percentage: {flagged_percentage:.2f}% ({results['Flag_for_Review'].sum()} samples)")

    # Separation of Ensemble Scores
    flagged_scores = test_ensemble_scores[results["Flag_for_Review"] == True]
    not_flagged_scores = test_ensemble_scores[results["Flag_for_Review"] == False]
    flagged_mean = np.mean(flagged_scores)
    flagged_std = np.std(flagged_scores)
    not_flagged_mean = np.mean(not_flagged_scores)
    not_flagged_std = np.std(not_flagged_scores)
    print("\nEnsemble Score Separation:")
    print(f"Flagged - Mean: {flagged_mean:.4f}, Std: {flagged_std:.4f}")
    print(f"Not Flagged - Mean: {not_flagged_mean:.4f}, Std: {not_flagged_std:.4f}")

    # Save evaluation metrics to file
    with open(os.path.join(output_dir, 'performance_metrics.txt'), 'w') as f:
        f.write("=== Model Performance Evaluation ===\n")
        f.write("Reconstruction Error (MAE) Statistics:\n")
        f.write(f"Training - Mean: {train_recon_mean:.6f}, Std: {train_recon_std:.6f}\n")
        f.write(f"Test - Mean: {test_recon_mean:.6f}, Std: {test_recon_std:.6f}\n")
        f.write("\nEpistemic Uncertainty Statistics:\n")
        f.write(f"Training - Mean: {train_epistemic_mean:.6f}, Std: {train_epistemic_std:.6f}\n")
        f.write(f"Test - Mean: {test_epistemic_mean:.6f}, Std: {test_epistemic_std:.6f}\n")
        f.write("\nAleatoric Uncertainty Statistics:\n")
        f.write(f"Training - Mean: {train_aleatoric_mean:.6f}, Std: {train_aleatoric_std:.6f}\n")
        f.write(f"Test - Mean: {test_aleatoric_mean:.6f}, Std: {test_aleatoric_std:.6f}\n")
        f.write(f"\nFlagged Percentage: {flagged_percentage:.2f}% ({results['Flag_for_Review'].sum()} samples)\n")
        f.write("\nEnsemble Score Separation:\n")
        f.write(f"Flagged - Mean: {flagged_mean:.4f}, Std: {flagged_std:.4f}\n")
        f.write(f"Not Flagged - Mean: {not_flagged_mean:.4f}, Std: {not_flagged_std:.4f}\n")

# Run evaluation
evaluate_model_performance(
    train_anomaly_scores_ae, test_anomaly_scores_ae, test_ensemble_scores, results,
    train_epistemic_uncertainty, test_epistemic_uncertainty,
    train_aleatoric_uncertainty, test_aleatoric_uncertainty
)
