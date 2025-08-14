import pandas as pd
import numpy as np

# Define scenarios based on the original code
SCENARIOS = [1, 2, 3, 4]

# Define key variables to summarize (based on DataCollector from original code)
AGENT_VARIABLES = [
    'SA', 'SA_P', 'SA_C', 'SA_J', 'Trust', 'Comm_Prob', 'Task_Familiarity', 
    'Workload', 'Fatigue', 'Competence_Level', 'Role_Clarity', 'Reporting_Threshold',
    'MM_Team', 'MM_Task', 'MM_Process', 'MM_Situation', 'MM_Competence', 
    'Info_Team', 'Info_Task', 'Info_Process', 'Info_Situation', 'Info_Competence',
    'Delta_SA', 'Scenario_Components', 'Initial_SA', 'Weight_P', 'Weight_C', 
    'Weight_J', 'Comp_Competence_P', 'Comp_Competence_C', 'Comp_Competence_J',
    'Detection_Accuracy', 'Comm_Effectiveness', 'Successful_Comms', 
    'Message_History_Count', 'Messages_Received', 'Convergence_Rate', 
    'Scenario_Learning_Mod', 'Previous_SA', 'Strength_P', 'Strength_C', 'Strength_J',
    'Trust_Partners', 'Avg_Trust_Per_Partner'
]

MODEL_VARIABLES = [
    'Avg_SA', 'SA_Director', 'SA_Manager', 'SA_Worker', 'Task_Complexity',
    'Avg_Org_Structure', 'Avg_SA_Change', 'Step_Count', 'Num_Agents'
]

# Output Excel file
OUTPUT_FILE = "single_iteration_summary.xlsx"

# Initialize Excel writer
writer = pd.ExcelWriter(OUTPUT_FILE, engine='xlsxwriter')

# Process each scenario
all_scenario_data = []
for scenario in SCENARIOS:
    # Read scenario data
    input_file = f"mathematical_sa_simulation_scenario_{scenario}.xlsx"
    try:
        df = pd.read_excel(input_file, sheet_name=f"Scenario_{scenario}")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found. Skipping scenario {scenario}.")
        continue
    
    # Filter for iteration 0
    iteration_0_data = df[df['Iteration'] == 0].copy()
    if iteration_0_data.empty:
        print(f"Warning: No data for iteration 0 in scenario {scenario}. Skipping.")
        continue
    
    # Save to individual sheet
    iteration_0_data.to_excel(writer, sheet_name=f"Scenario_{scenario}_Iter0", index=False)
    print(f"Saved iteration 0 data for scenario {scenario} to sheet 'Scenario_{scenario}_Iter0'")
    
    # Store for summary
    all_scenario_data.append(iteration_0_data)

# Create summary sheet with averages across scenarios
if all_scenario_data:
    # Concatenate all scenario data for iteration 0
    combined_data = pd.concat(all_scenario_data, ignore_index=True)
    
    # Group by Step and Role to compute averages for agent-level variables
    summary_data = []
    for step in combined_data['Step'].unique():
        for role in combined_data['Role'].unique():
            step_role_data = combined_data[(combined_data['Step'] == step) & (combined_data['Role'] == role)]
            if not step_role_data.empty:
                means = step_role_data[AGENT_VARIABLES].mean()
                summary_row = {'Step': step, 'Role': role}
                summary_row.update({var: means.get(var, np.nan) for var in AGENT_VARIABLES})
                summary_data.append(summary_row)
    
    # Convert to DataFrame
    summary_df = pd.DataFrame(summary_data)
    
    # Save summary to Excel
    summary_df.to_excel(writer, sheet_name='Agent_Variables_Summary', index=False)
    print("Saved agent-level variables summary to sheet 'Agent_Variables_Summary'")

# Process model-level variables from summary file
try:
    summary_file = "mathematical_sa_simulation_summary.xlsx"
    summary_stats = pd.read_excel(summary_file, sheet_name="Summary")
    
    # Filter for iteration 0 across all scenarios
    model_summary = summary_stats[summary_stats['Iteration'] == 0].copy()
    
    # Compute averages for model-level variables
    model_summary_means = model_summary[['Scenario', 'Avg_SA_Change', 'SA_Change_Directors', 
                                        'SA_Change_Managers', 'SA_Change_Workers']].groupby('Scenario').mean()
    
    # Add overall averages
    overall_means = model_summary[['Avg_SA_Change', 'SA_Change_Directors', 
                                  'SA_Change_Managers', 'SA_Change_Workers']].mean()
    overall_means = pd.DataFrame([overall_means], index=['Overall'])
    
    # Combine scenario-specific and overall averages
    model_summary_final = pd.concat([model_summary_means, overall_means])
    
    # Save to Excel
    model_summary_final.to_excel(writer, sheet_name='Model_Variables_Summary')
    print("Saved model-level variables summary to sheet 'Model_Variables_Summary'")
except FileNotFoundError:
    print(f"Error: Summary file {summary_file} not found. Skipping model-level summary.")

# Save and close Excel file
writer.close()
print(f"\nAll data saved to {OUTPUT_FILE}")
