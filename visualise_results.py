import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Set style for clear and legible plots
plt.style.use('seaborn')
sns.set_context("notebook", font_scale=1.2)

# Load data from Excel
summary_file = "mathematical_sa_simulation_summary.xlsx"
summary_df = pd.read_excel(summary_file, sheet_name="Summary")
stats_df = pd.read_excel(summary_file, sheet_name="Statistical_Tests")
scenario_stats_df = pd.read_excel(summary_file, sheet_name="Scenario_Statistics")

# Create output directory for plots
output_dir = Path("simulation_plots")
output_dir.mkdir(exist_ok=True)

# Plot 1: Scenario Performance Comparison (Bar Plot with Confidence Intervals)
plt.figure(figsize=(10, 6))
scenario_means = summary_df.groupby('Scenario')['Avg_SA_Change'].agg(['mean', 'std', 'count']).reset_index()
scenario_means['se'] = scenario_means['std'] / np.sqrt(scenario_means['count'])
scenario_means['ci_95'] = 1.96 * scenario_means['se']

bars = plt.bar(scenario_means['Scenario'], scenario_means['mean'], yerr=scenario_means['ci_95'], 
               capsize=5, color=sns.color_palette("Blues", n_colors=len(scenario_means)))
plt.xlabel('Scenario', fontsize=14)
plt.ylabel('Mean SA Change', fontsize=14)
plt.title('Scenario Performance Comparison with 95% Confidence Intervals', fontsize=16, pad=15)
plt.xticks(scenario_means['Scenario'], [f"Scenario {s}" for s in scenario_means['Scenario']], fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.3f}', 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig(output_dir / "scenario_performance.jpg", dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Role-Specific SA Changes (Line Plot)
plt.figure(figsize=(12, 8))
roles = ['SA_Change_Directors', 'SA_Change_Managers', 'SA_Change_Workers']
colors = sns.color_palette("husl", n_colors=len(roles))
for role, color in zip(roles, colors):
    role_data = summary_df.groupby('Scenario')[role].mean().reset_index()
    plt.plot(role_data['Scenario'], role_data[role], marker='o', linewidth=2, 
             markersize=8, label=role.replace('SA_Change_', ''), color=color)

plt.xlabel('Scenario', fontsize=14)
plt.ylabel('Mean SA Change', fontsize=14)
plt.title('Role-Specific SA Changes Across Scenarios', fontsize=16, pad=15)
plt.xticks(scenario_means['Scenario'], [f"Scenario {s}" for s in scenario_means['Scenario']], fontsize=12)
plt.legend(title='Role', fontsize=12, title_fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(output_dir / "role_specific_sa_changes.jpg", dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: Statistical Significance Heatmap (P-Values for Pairwise Comparisons)
pairwise_tests = stats_df[stats_df['Test'].str.contains("t-test")]
pivot_data = pairwise_tests.pivot_table(values='P_Value', index='Role', columns='Test')
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_data, annot=True, fmt='.4f', cmap='Reds', cbar_kws={'label': 'P-Value'},
            annot_kws={'size': 10})
plt.title('P-Values for Pairwise Scenario Comparisons', fontsize=16, pad=15)
plt.xlabel('Comparison', fontsize=14)
plt.ylabel('Role', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig(output_dir / "statistical_significance_heatmap.jpg", dpi=300, bbox_inches='tight')
plt.close()

# Plot 4: SA Change Distribution by Scenario and Role (Box Plot)
plt.figure(figsize=(12, 8))
melted_df = summary_df.melt(id_vars=['Scenario'], 
                            value_vars=['SA_Change_Directors', 'SA_Change_Managers', 'SA_Change_Workers'],
                            var_name='Role', value_name='SA_Change')
melted_df['Role'] = melted_df['Role'].str.replace('SA_Change_', '')
sns.boxplot(x='Scenario', y='SA_Change', hue='Role', data=melted_df, palette='Set2')
plt.xlabel('Scenario', fontsize=14)
plt.ylabel('SA Change', fontsize=14)
plt.title('Distribution of SA Changes by Scenario and Role', fontsize=16, pad=15)
plt.xticks(fontsize=12)
plt.legend(title='Role', fontsize=12, title_fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(output_dir / "sa_change_distribution.jpg", dpi=300, bbox_inches='tight')
plt.close()

print(f"Plots saved to {output_dir}:")
print("- scenario_performance.jpg")
print("- role_specific_sa_changes.jpg")
print("- statistical_significance_heatmap.jpg")
print("- sa_change_distribution.jpg")