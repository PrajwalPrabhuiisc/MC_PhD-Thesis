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
    # Read scenario data for agent-level variables
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
    
    # Save raw iteration 0 data to individual sheet
    iteration_0_data.to_excel(writer, sheet_name=f"Scenario_{scenario}_Iter0", index=False)
    print(f"Saved iteration 0 data for scenario {scenario} to sheet 'Scenario_{scenario}_Iter0'")
    
    # Create agent-level summary for this scenario
    summary_data = []
    for step in iteration_0_data['Step'].unique():
        for role in iteration_0_data['Role'].unique():
            step_role_data = iteration_0_data[(iteration_0_data['Step'] == step) & (iteration_0_data['Role'] == role)]
            if not step_role_data.empty:
                means = step_role_data[AGENT_VARIABLES].mean()
                summary_row = {'Step': step, 'Role': role}
                summary_row.update({var: means.get(var, np.nan) for var in AGENT_VARIABLES})
                summary_data.append(summary_row)
    
    # Convert to DataFrame and save to scenario-specific agent summary sheet
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name=f"Scenario_{scenario}_Agent_Summary", index=False)
        print(f"Saved agent-level summary for scenario {scenario} to sheet 'Scenario_{scenario}_Agent_Summary'")
    
    # Store for potential further use
    all_scenario_data.append(iteration_0_data)

# Process model-level variables from summary file for each scenario
try:
    summary_file = "mathematical_sa_simulation_summary.xlsx"
    summary_stats = pd.read_excel(summary_file, sheet_name="Summary")
    
    # Filter for iteration 0 across all scenarios
    model_summary = summary_stats[summary_stats['Iteration'] == 0].copy()
    
    # Process each scenario separately
    for scenario in SCENARIOS:
        scenario_model_data = model_summary[model_summary['Scenario'] == scenario].copy()
        if scenario_model_data.empty:
            print(f"Warning: No model data for iteration 0 in scenario {scenario}. Skipping model-level summary.")
            continue
        
        # Compute averages for model-level variables for this scenario
        scenario_model_summary = []
        for step in scenario_model_data['Step'].unique():
            step_data = scenario_model_data[scenario_model_data['Step'] == step]
            if not step_data.empty:
                means = step_data[MODEL_VARIABLES].mean()
                summary_row = {'Step': step}
                summary_row.update({var: means.get(var, np.nan) for var in MODEL_VARIABLES})
                scenario_model_summary.append(summary_row)
        
        # Convert to DataFrame and save to scenario-specific model summary sheet
        if scenario_model_summary:
            scenario_model_df = pd.DataFrame(scenario_model_summary)
            scenario_model_df.to_excel(writer, sheet_name=f"Scenario_{scenario}_Model_Summary", index=False)
            print(f"Saved model-level summary for scenario {scenario} to sheet 'Scenario_{scenario}_Model_Summary'")
except FileNotFoundError:
    print(f"Error: Summary file {summary_file} not found. Skipping model-level summaries.")

# Save and close Excel file
writer.close()
print(f"\nAll data saved to {OUTPUT_FILE}")
