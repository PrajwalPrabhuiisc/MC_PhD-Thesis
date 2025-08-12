import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Constants
SCENARIOS = [1, 2, 3, 4]
ITERATION = 0  # Visualize the first iteration
VARIABLE_GROUPS = {
    "SA Related": ['SA', 'SA_P', 'SA_C', 'SA_J', 'Delta_SA'],
    "Mental Model Related": ['MM_Team', 'MM_Task', 'MM_Process', 'MM_Situation', 'MM_Competence'],
    "Information Related": ['Info_Team', 'Info_Task', 'Info_Process', 'Info_Situation', 'Info_Competence'],
    "Other Variables": ['Trust', 'Comm_Prob', 'Task_Familiarity', 'Workload', 'Fatigue', 'Competence_Level']
}
ROLES = ['Director', 'Manager', 'Worker']
BASE_OUTPUT_DIR = 'journal_manuscript_visualizations'
PLOTS_PER_FIGURE = 6  # 2x3 grid for most cases, adjusted for 5 or fewer variables

# Create base output directory
if not os.path.exists(BASE_OUTPUT_DIR):
    os.makedirs(BASE_OUTPUT_DIR)

# Plotting function
def create_grouped_plots(scenario, df, group_name, variables):
    # Create scenario-specific directory
    scenario_dir = os.path.join(BASE_OUTPUT_DIR, f'scenario_{scenario}')
    if not os.path.exists(scenario_dir):
        os.makedirs(scenario_dir)
    
    # Filter data for the specific iteration
    iteration_data = df[df['Iteration'] == ITERATION]
    
    # Set up professional plot style
    plt.style.use('seaborn-whitegrid')
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['figure.figsize'] = (12, 8)
    
    # Calculate number of subplots needed
    num_vars = len(variables)
    rows = math.ceil(num_vars / 3)  # 3 columns max
    cols = min(num_vars, 3)
    
    # Create figure
    fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows), sharex=True)
    axes = axes.flatten() if rows > 1 else [axes]
    
    for idx, variable in enumerate(variables):
        ax = axes[idx]
        for role in ROLES:
            role_data = iteration_data[iteration_data['Role'] == role]
            if not role_data.empty:
                sns.lineplot(x='Step', y=variable, data=role_data, label=role, ax=ax, linewidth=1.5)
        
        ax.set_title(f'{variable}', pad=10)
        ax.set_xlabel('Step')
        ax.set_ylabel(variable)
        ax.legend(title='Role', frameon=True, loc='best')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Hide unused subplots
    for idx in range(num_vars, len(axes)):
        axes[idx].set_visible(False)
    
    # Adjust layout
    plt.tight_layout(pad=2.0)
    
    # Save the plot
    output_file = os.path.join(scenario_dir, f'scenario_{scenario}_{group_name.replace(" ", "_")}_iteration_{ITERATION}.jpg')
    plt.savefig(output_file, format='jpg', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved plot for Scenario {scenario}, {group_name} to {output_file}")

# Main execution
for scenario in SCENARIOS:
    # Load scenario data
    input_file = f"mathematical_sa_simulation_scenario_{scenario}.xlsx"
    try:
        df = pd.read_excel(input_file)
        print(f"Processing Scenario {scenario}...")
        for group_name, variables in VARIABLE_GROUPS.items():
            create_grouped_plots(scenario, df, group_name, variables)
    except FileNotFoundError:
        print(f"Data file for Scenario {scenario} not found. Skipping...")

print("\nVisualization complete. Plots saved in scenario-specific folders under 'journal_manuscript_visualizations'.")