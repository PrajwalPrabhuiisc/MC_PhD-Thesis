import os
import logging
from concurrent.futures import ProcessPoolExecutor, as_completed
from construction_model import ConstructionModel
from enums import ReportingStructure, OrgStructure, AgentRole
import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
from analyse_h1 import analyze_h1, load_simulation_data

# Set up logging (console for faster debugging)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_simulation_config(run_id: int, reporting_structure: str, org_structure: str, steps: int = 100) -> dict:
    """Run a single simulation configuration and return results."""
    # Define simulation parameters
    width = 20
    height = 20
    hazard_prob = 0.01  # For ~1–2 safety incidents
    delay_prob = 0.015  # For ~1 task/step
    resource_prob = 0.05
    comm_failure_dedicated = 0.05
    comm_failure_self = 0.05
    comm_failure_none = 0.10
    worker_detection = 0.80
    manager_detection = 0.90
    reporter_detection = 0.95
    director_detection = 0.85
    worker_reporting = 0.80
    manager_reporting = 0.90
    reporter_reporting = 0.95
    director_reporting = 0.85
    initial_budget = 1000000
    initial_equipment = 500

    # Log simulation start
    logging.info(f"Run {run_id}: Starting simulation: {reporting_structure}/{org_structure}, steps={steps}")

    try:
        # Initialize the model
        model = ConstructionModel(
            width=width,
            height=height,
            reporting_structure=reporting_structure,
            org_structure=org_structure,
            hazard_prob=hazard_prob,
            delay_prob=delay_prob,
            resource_prob=resource_prob,
            comm_failure_dedicated=comm_failure_dedicated,
            comm_failure_self=comm_failure_self,
            comm_failure_none=comm_failure_none,
            worker_detection=worker_detection,
            manager_detection=manager_detection,
            reporter_detection=reporter_detection,
            director_detection=director_detection,
            worker_reporting=worker_reporting,
            manager_reporting=manager_reporting,
            reporter_reporting=reporter_reporting,
            director_reporting=director_reporting,
            initial_budget=initial_budget,
            initial_equipment=initial_equipment
        )

        # Log agent counts
        agent_counts = {
            "Workers": len([a for a in model.schedule.agents if a.role == AgentRole.WORKER]),
            "Managers": len([a for a in model.schedule.agents if a.role == AgentRole.MANAGER]),
            "Directors": len([a for a in model.schedule.agents if a.role == AgentRole.DIRECTOR]),
            "Reporters": len([a for a in model.schedule.agents if a.role == AgentRole.REPORTER])
        }
        logging.info(f"Run {run_id}: Agent counts for {reporting_structure}/{org_structure}: {agent_counts}")

        # Run the simulation
        model.run_simulation(steps)

        # Collect results
        schedule_adherence = (
            model.outcomes.tasks_completed_on_time / model.outcomes.total_tasks * 100
            if model.outcomes.total_tasks > 0 else 0
        )
        average_sa = np.mean([a.awareness.total_score() for a in model.schedule.agents])
        results = {
            "Run_ID": run_id,
            "Simulation_ID": model.simulation_id,
            "Reporting_Structure": reporting_structure,
            "Org_Structure": org_structure,
            "Steps": steps,
            "Safety_Incidents": model.outcomes.safety_incidents,
            "Total_Tasks": model.outcomes.total_tasks,
            "Tasks_Completed_On_Time": model.outcomes.tasks_completed_on_time,
            "Schedule_Adherence": schedule_adherence,
            "Budget_Remaining": model.budget,
            "Equipment_Available": model.equipment_available,
            "Average_SA": average_sa,
            "Excel_File": os.path.join(os.getcwd(), "simulation_outputs", f"construction_simulation_{model.simulation_id}.xlsx")
        }
        logging.info(f"Run {run_id}: Completed simulation: {reporting_structure}/{org_structure}. Results: {results}")
        return results

    except Exception as e:
        logging.error(f"Run {run_id}: Error in {reporting_structure}/{org_structure}: {str(e)}")
        return {
            "Run_ID": run_id,
            "Simulation_ID": "failed",
            "Reporting_Structure": reporting_structure,
            "Org_Structure": org_structure,
            "Steps": steps,
            "Error": str(e)
        }

def compute_statistics(results: list) -> pd.DataFrame:
    """Compute statistical metrics (mean, std, 95% CI) for each configuration."""
    df = pd.DataFrame(results)
    stats_data = []
    metrics = ["Safety_Incidents", "Total_Tasks", "Schedule_Adherence", "Budget_Remaining", "Equipment_Available", "Average_SA"]
    
    for (reporting, org), group in df.groupby(["Reporting_Structure", "Org_Structure"]):
        if "Error" not in group.columns or not group["Error"].notna().any():
            stat_row = {
                "Reporting_Structure": reporting,
                "Org_Structure": org,
                "Runs_Completed": len(group)
            }
            for metric in metrics:
                values = group[metric].dropna().astype(float)
                mean = values.mean()
                std = values.std()
                ci = stats.t.interval(
                    alpha=0.95,
                    df=len(values)-1,
                    loc=mean,
                    scale=std/np.sqrt(len(values)) if len(values) > 1 else 0
                ) if len(values) > 1 else (mean, mean)
                stat_row[f"{metric}_Mean"] = mean
                stat_row[f"{metric}_Std"] = std
                stat_row[f"{metric}_CI_Lower"] = ci[0]
                stat_row[f"{metric}_CI_Upper"] = ci[1]
            stats_data.append(stat_row)
        else:
            stat_row = {
                "Reporting_Structure": reporting,
                "Org_Structure": org,
                "Runs_Completed": len(group[group["Error"].isna()]),
                "Error": group["Error"].dropna().tolist()
            }
            stats_data.append(stat_row)
    
    return pd.DataFrame(stats_data)

def save_results(all_results: list, stats_df: pd.DataFrame):
    """Save raw results and statistical summary to CSV files."""
    output_dir = os.path.join(os.getcwd(), "simulation_outputs")
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save raw results
    raw_file = os.path.join(output_dir, f"simulation_summary_{timestamp}.csv")
    pd.DataFrame(all_results).to_csv(raw_file, index=False)
    logging.info(f"Raw results saved to {raw_file}")
    
    # Save statistical summary
    stats_file = os.path.join(output_dir, f"statistical_summary_{timestamp}.csv")
    stats_df.to_csv(stats_file, index=False)
    logging.info(f"Statistical summary saved to {stats_file}")

if __name__ == "__main__":
    # Define configurations to test (flat org_structure only)
    configurations = [
        ("dedicated", "flat"),
        ("self", "flat"),
        ("none", "flat")
    ]

    steps = 100  # Align with analyse_h1.py expectation
    num_runs = 60  # Number of runs per configuration

    # Run simulations in parallel
    all_results = []
    with ProcessPoolExecutor(max_workers=4) as executor:  # Limit to 4 workers to manage memory
        futures = [
            executor.submit(run_simulation_config, run_id, reporting, org, steps)
            for reporting, org in configurations
            for run_id in range(1, num_runs + 1)
        ]
        for future in as_completed(futures):
            result = future.result()
            all_results.append(result)
            print(f"Run {result['Run_ID']}: Completed {result['Reporting_Structure']}/{result['Org_Structure']}, "
                  f"Safety Incidents={result.get('Safety_Incidents', 'N/A')}, "
                  f"Total Tasks={result.get('Total_Tasks', 'N/A')}, "
                  f"Adherence={result.get('Schedule_Adherence', 'N/A'):.2f}%, "
                  f"Average SA={result.get('Average_SA', 'N/A'):.2f}")

    # Compute and save statistics
    stats_df = compute_statistics(all_results)
    save_results(all_results, stats_df)
    print(f"All {num_runs * len(configurations)} simulations completed. Results and statistics saved to simulation_outputs.")
    
    # Print statistical summary
    print("\nStatistical Summary:")
    for _, row in stats_df.iterrows():
        print(f"\n{row['Reporting_Structure']}/{row['Org_Structure']} (Runs: {row['Runs_Completed']}):")
        if "Error" not in row or pd.isna(row["Error"]):
            print(f"  Safety_Incidents: Mean={row['Safety_Incidents_Mean']:.2f}, "
                  f"Std={row['Safety_Incidents_Std']:.2f}, "
                  f"95% CI=({row['Safety_Incidents_CI_Lower']:.2f}, {row['Safety_Incidents_CI_Upper']:.2f})")
            print(f"  Total_Tasks: Mean={row['Total_Tasks_Mean']:.2f}, "
                  f"Std={row['Total_Tasks_Std']:.2f}, "
                  f"95% CI=({row['Total_Tasks_CI_Lower']:.2f}, {row['Total_Tasks_CI_Upper']:.2f})")
            print(f"  Schedule_Adherence: Mean={row['Schedule_Adherence_Mean']:.2f}%, "
                  f"Std={row['Schedule_Adherence_Std']:.2f}, "
                  f"95% CI=({row['Schedule_Adherence_CI_Lower']:.2f}, {row['Schedule_Adherence_CI_Upper']:.2f})")
            print(f"  Average_SA: Mean={row['Average_SA_Mean']:.2f}, "
                  f"Std={row['Average_SA_Std']:.2f}, "
                  f"95% CI=({row['Average_SA_CI_Lower']:.2f}, {row['Average_SA_CI_Upper']:.2f})")
        else:
            print(f"  Errors: {row['Error']}")

    # Perform statistical significance testing on SA scores
    print("\nRunning statistical significance test on Situational Awareness...")
    try:
        metrics_df, agent_df = load_simulation_data()
        analyze_h1(metrics_df, agent_df)
    except Exception as e:
        logging.error(f"Statistical analysis failed: {e}")
        print(f"Error during statistical analysis: {e}")