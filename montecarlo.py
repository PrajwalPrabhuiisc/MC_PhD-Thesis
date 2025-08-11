import numpy as np
import pandas as pd
from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.datacollection import DataCollector
from scipy import stats
import uuid
import itertools
import random
import math

# Constants
NUM_DIRECTORS = 3
NUM_MANAGERS = 7
NUM_WORKERS = 20
NUM_AGENTS = NUM_DIRECTORS + NUM_MANAGERS + NUM_WORKERS
NUM_STEPS = 150
NUM_ITERATIONS = 200
REPORTING_THRESHOLD = {"Worker": 0.3, "Manager": 0.5, "Director": 0.7}
NOISE_STD = {"reporting": 0.03, "communication": 0.02, "mental_model": 0.02}
LEARNING_RATE = 0.25
DETECTION_ACCURACY = {"Worker": 0.8, "Manager": 0.9, "Director": 0.85}

# Scenario definitions
SCENARIO_WEIGHTS = {
    1: {"Worker": {"P": 1.0}, "Manager": {"P": 1.0}, "Director": {"P": 1.0}},
    2: {"Worker": {"P": 0.6, "C": 0.4}, "Manager": {"P": 0.6, "C": 0.4}, "Director": {"P": 0.6, "C": 0.4}},
    3: {"Worker": {"P": 0.3, "C": 0.3, "J": 0.4}, "Manager": {"P": 0.3, "C": 0.3, "J": 0.4}, "Director": {"P": 0.3, "C": 0.3, "J": 0.4}},
    4: {"Worker": {"P": 1.0}, "Manager": {"P": 0.6, "C": 0.4}, "Director": {"P": 0.3, "C": 0.3, "J": 0.4}}
}

SCENARIOS = {
    1: {"Worker": ["P"], "Manager": ["P"], "Director": ["P"]},
    2: {"Worker": ["P", "C"], "Manager": ["P", "C"], "Director": ["P", "C"]},
    3: {"Worker": ["P", "C", "J"], "Manager": ["P", "C", "J"], "Director": ["P", "C", "J"]},
    4: {"Worker": ["P"], "Manager": ["P", "C"], "Director": ["P", "C", "J"]}
}

COMPONENT_SYNERGY = {
    "P": {"P": 1.0, "C": 0.3, "J": 0.2},
    "C": {"P": 0.4, "C": 1.0, "J": 0.5},
    "J": {"P": 0.2, "C": 0.6, "J": 1.0}
}

ROLE_BASE_MULTIPLIERS = {
    "Worker": {"P": 1.0, "C": 0.7, "J": 0.5},
    "Manager": {"P": 1.1, "C": 1.0, "J": 0.8},
    "Director": {"P": 1.2, "C": 1.2, "J": 1.0}
}

class MentalModel:
    def __init__(self):
        self.values = np.random.uniform(0.4, 0.6, 5)
        self.convergence_rate = np.random.uniform(0.1, 0.3)

    def update(self, delta, scenario_components, noise_std=NOISE_STD["mental_model"]):
        component_boost = 1.0 + 0.2 * len(scenario_components)
        noise = np.random.normal(0, noise_std, 5)
        learning_modifier = LEARNING_RATE * component_boost * self.convergence_rate
        self.values = np.clip(self.values + learning_modifier * delta + noise, 0, 1)
        self.convergence_rate = max(0.05, self.convergence_rate * 0.995)

    def cosine_similarity(self, other_model):
        norm = np.linalg.norm(self.values) * np.linalg.norm(other_model)
        return np.dot(self.values, other_model) / norm if norm != 0 else 0

class SituationalAwareness:
    def __init__(self, scenario_components):
        self.perception = np.random.uniform(5, 15)
        self.comprehension = np.random.uniform(5, 15)
        self.projection = np.random.uniform(5, 15)
        self.scenario_components = scenario_components
        self.component_strengths = {comp: np.random.uniform(0.8, 1.2) for comp in scenario_components}
        self.sa = self._calculate_weighted_sa()
        self.previous_sa = self.sa

    def _calculate_weighted_sa(self):
        base_components = {"P": self.perception, "C": self.comprehension, "J": self.projection}
        if len(self.scenario_components) == 1:
            comp = self.scenario_components[0]
            return base_components[comp] * self.component_strengths.get(comp, 1.0)
        
        weighted_sum = 0
        total_weight = 0
        for comp1 in self.scenario_components:
            base_value = base_components[comp1]
            strength = self.component_strengths.get(comp1, 1.0)
            synergy_boost = 1.0
            for comp2 in self.scenario_components:
                if comp1 != comp2:
                    synergy_boost += COMPONENT_SYNERGY[comp1][comp2] * 0.3
            weighted_sum += base_value * strength * synergy_boost
            total_weight += strength * synergy_boost
        return weighted_sum / max(total_weight, 1.0) if total_weight > 0 else 0

    def update(self, perception, comprehension, projection):
        self.perception = perception
        self.comprehension = comprehension
        self.projection = projection
        self.previous_sa = self.sa
        self.sa = self._calculate_weighted_sa()
        self.sa = np.clip(self.sa, 0, 100)

class Communication:
    def __init__(self, role, communication_prob, scenario_components, scenario_weights):
        self.role = role
        self.communication_prob = communication_prob
        self.messages = []
        self.scenario_components = scenario_components
        self.scenario_weights = scenario_weights
        self.message_history = []
        self.communication_effectiveness = np.random.uniform(0.7, 1.0)
        self.successful_communications = 0  # Track successful communications

    def generate_report(self, sa_components, information, sa, trust, threshold):
        if sa >= threshold and np.random.random() < self.communication_prob:
            sa_values = {"P": sa_components.perception, "C": sa_components.comprehension, "J": sa_components.projection}
            weighted_sa = 0
            total_weight = 0
            for component in self.scenario_components:
                weight = self.scenario_weights[component]
                value = sa_values[component]
                role_multiplier = ROLE_BASE_MULTIPLIERS[self.role][component]
                weighted_sa += weight * value * role_multiplier
                total_weight += weight * role_multiplier
            if total_weight > 0:
                weighted_sa /= total_weight
            effectiveness = self.communication_effectiveness * trust
            noise = np.random.normal(0, NOISE_STD["reporting"], 5)
            report = information * (weighted_sa / 100.0) * effectiveness + noise
            self.message_history.append(weighted_sa)
            if len(self.message_history) > 10:
                self.message_history.pop(0)
                self.communication_effectiveness = min(1.0, self.communication_effectiveness + 0.01)
            self.successful_communications += 1  # Increment on successful report
            return np.clip(report, 0, 1)
        return None

    def receive_message(self, message, sender_competence):
        if message is not None:
            noise = np.random.normal(0, NOISE_STD["communication"], 5)
            # Weight message by sender's competence
            processed_message = np.clip(message * sender_competence + noise, 0, 1)
            self.messages.append(processed_message)

class OrgAgent(Agent):
    def __init__(self, unique_id, model, role, scenario_components, scenario_weights):
        super().__init__(unique_id, model)
        self.role = role
        self.scenario_components = scenario_components
        self.scenario_weights = scenario_weights
        self.trust = {}  # Dictionary to track trust in other agents
        self.communication_prob = np.random.uniform(0.75, 0.95)
        self.task_familiarity = np.random.uniform(0.5, 0.9)
        self.workload = np.random.uniform(0.5, 3.5)
        self.fatigue = np.random.uniform(0.1, 0.7)
        self.competence_level = np.random.uniform(0.6, 0.9)
        self.detection_accuracy = DETECTION_ACCURACY[role]
        self.role_clarity = np.random.uniform(0.5, 0.8)  # Phase 2: Dynamic role clarity
        self.component_competence = {comp: ROLE_BASE_MULTIPLIERS[role][comp] * np.random.uniform(0.8, 1.2) for comp in ["P", "C", "J"]}
        self.mental_model = MentalModel()
        self.sa = SituationalAwareness(scenario_components)
        self.communication = Communication(role, self.communication_prob, scenario_components, scenario_weights)
        self.information = np.random.uniform(0.3, 0.9, 5)
        self.initial_sa = self.sa.sa
        self.scenario_learning_modifier = 1.0 + 0.1 * len(scenario_components)
        self.reporting_threshold = REPORTING_THRESHOLD[role]  # Phase 3: Adaptive threshold
        # Initialize trust network
        for agent in model.schedule.agents:
            if agent != self:
                self.trust[agent.unique_id] = np.random.uniform(0.6, 0.95)

    def observe_event(self):
        severity = self.model.task_complexity
        for component in ["P", "C", "J"]:
            base_gain = self._calculate_base_gain(component, severity)
            if component in self.scenario_components:
                scenario_boost = 2.0 * self.scenario_learning_modifier
                component_competence = self.component_competence[component]
                final_gain = base_gain * scenario_boost * component_competence
            else:
                final_gain = base_gain * 0.3
            if component == "P":
                self.sa.perception = min(self.sa.perception + final_gain, 100)
            elif component == "C":
                self.sa.comprehension = min(self.sa.comprehension + final_gain, 100)
            elif component == "J":
                self.sa.projection = min(self.sa.projection + final_gain, 100)
        # Phase 2: Update role clarity based on experience
        self.role_clarity = min(1.0, self.role_clarity + 0.01 * len(self.scenario_components) * self.competence_level)

    def _calculate_base_gain(self, component, severity):
        base_values = {"P": 8.0, "C": 6.0, "J": 5.0}
        base = base_values[component]
        competence_modifier = 1.0 + self.competence_level
        detection_modifier = self.detection_accuracy
        fatigue_penalty = 1.0 - (self.fatigue * 0.3)
        workload_penalty = 1.0 - (self.workload / 10.0)
        org_feedback = 1.0 + (self.model.avg_sa_change / 100.0) * 0.5
        role_clarity_boost = 1.0 + self.role_clarity * 0.5  # Phase 2: Role clarity impact
        noise_std = 0.1 + 0.2 * self.fatigue
        noise = max(-0.3, min(0.3, np.random.normal(0, noise_std)))
        return base * severity * competence_modifier * detection_modifier * fatigue_penalty * workload_penalty * org_feedback * role_clarity_boost * (1 + noise)

    def execute_action(self, action):
        severity = self.model.task_complexity
        action_multiplier = 0.7 if action == "ACT" else 0.5
        for component in ["P", "C", "J"]:
            base_gain = self._calculate_base_gain(component, severity) * action_multiplier
            if component in self.scenario_components:
                scenario_boost = 1.5 * self.scenario_learning_modifier
                final_gain = base_gain * scenario_boost * self.component_competence[component]
            else:
                final_gain = base_gain * 0.2
            if component == "P":
                self.sa.perception = min(self.sa.perception + final_gain, 100)
            elif component == "C":
                self.sa.comprehension = min(self.sa.comprehension + final_gain, 100)
            elif component == "J":
                self.sa.projection = min(self.sa.projection + final_gain, 100)

    def update_trust(self, partner, message_success):
        # Phase 2: Dynamic trust update based on communication success
        trust_change = 0.02 if message_success else -0.02
        self.trust[partner.unique_id] = np.clip(self.trust[partner.unique_id] + trust_change, 0.1, 1.0)

    def communicate(self):
        # Phase 3: Adaptive reporting threshold
        self.reporting_threshold = max(0.1, self.reporting_threshold - 0.01 * (self.sa.sa / 100.0) * self.role_clarity)
        report = self.communication.generate_report(self.sa, self.information, self.sa.sa, np.mean(list(self.trust.values())), self.reporting_threshold)
        if report is not None:
            partners = self.model.get_communication_partners(self)
            # Phase 2: Skill-based deference - prioritize competent partners
            partners = sorted(partners, key=lambda x: x.competence_level * self.trust[x.unique_id], reverse=True)[:5]
            for partner in partners:
                partner.communication.receive_message(report, self.competence_level)
                self.update_trust(partner, True)  # Update trust on successful communication
            action_threshold = 30 + 10 * len(self.scenario_components)
            action = "ACT" if self.sa.sa > action_threshold else "ESCALATE"
            self.execute_action(action)
        else:
            # Reduce trust for failed communications
            for partner in self.model.get_communication_partners(self):
                self.update_trust(partner, False)

    def update_mental_model(self):
        if self.communication.messages:
            avg_message = np.mean(self.communication.messages, axis=0)
            delta_mm = avg_message - self.mental_model.values
            self.mental_model.update(delta_mm, self.scenario_components)
            self.communication.messages = []

    def step(self):
        self.communicate()

    def advance(self):
        self.observe_event()
        self.sa.update(self.sa.perception, self.sa.comprehension, self.sa.projection)
        self.update_mental_model()

    def get_data(self):
        return {
            "Role": self.role,
            "SA": self.sa.sa,
            "SA_P": self.sa.perception,
            "SA_C": self.sa.comprehension,
            "SA_J": self.sa.projection,
            "Trust": np.mean(list(self.trust.values())),
            "Comm_Prob": self.communication_prob,
            "Task_Familiarity": self.task_familiarity,
            "Workload": self.workload,
            "Fatigue": self.fatigue,
            "Competence_Level": self.competence_level,
            "Role_Clarity": self.role_clarity,
            "Reporting_Threshold": self.reporting_threshold,
            "MM_Team": self.mental_model.values[0],
            "MM_Task": self.mental_model.values[1],
            "MM_Process": self.mental_model.values[2],
            "MM_Situation": self.mental_model.values[3],
            "MM_Competence": self.mental_model.values[4],
            "Info_Team": self.information[0],
            "Info_Task": self.information[1],
            "Info_Process": self.information[2],
            "Info_Situation": self.information[3],
            "Info_Competence": self.information[4],
            "Delta_SA": self.sa.sa - self.initial_sa,
            "Scenario_Components": len(self.scenario_components)
        }

class OrgModel(Model):
    def __init__(self, scenario):
        self.num_agents = NUM_AGENTS
        self.schedule = SimultaneousActivation(self)
        self.task_complexity = np.random.uniform(0.6, 0.9)
        self.true_mental_model = np.ones(5) * 0.8
        self.true_information = np.ones(5) * 0.9
        self.scenario = scenario
        self.avg_sa_change = 0.0
        self.step_count = 0
        self.org_structure = np.zeros((NUM_AGENTS, NUM_AGENTS))
        roles = ["Director"] * NUM_DIRECTORS + ["Manager"] * NUM_MANAGERS + ["Worker"] * NUM_WORKERS
        
        # Phase 3: Dynamic communication structure
        for i in range(NUM_AGENTS):
            for j in range(NUM_AGENTS):
                if i != j:
                    if (roles[i] == "Worker" and roles[j] == "Manager") or \
                       (roles[i] == "Manager" and roles[j] in ["Worker", "Director"]) or \
                       (roles[i] == "Director" and roles[j] == "Manager"):
                        self.org_structure[i, j] = np.random.uniform(0.5, 1.0)  # Weighted connections
                    elif roles[i] == "Worker" and roles[j] == "Worker" and np.random.random() < 0.1:
                        self.org_structure[i, j] = np.random.uniform(0.2, 0.5)

        for i, role in enumerate(roles):
            agent = OrgAgent(i, self, role, SCENARIOS[scenario][role], SCENARIO_WEIGHTS[scenario][role])
            self.schedule.add(agent)

        self.datacollector = DataCollector(
            agent_reporters={
                "Role": lambda a: a.role,
                "SA": lambda a: a.sa.sa,
                "SA_P": lambda a: a.sa.perception,
                "SA_C": lambda a: a.sa.comprehension,
                "SA_J": lambda a: a.sa.projection,
                "Trust": lambda a: np.mean(list(a.trust.values())),
                "Comm_Prob": lambda a: a.communication_prob,
                "Task_Familiarity": lambda a: a.task_familiarity,
                "Workload": lambda a: a.workload,
                "Fatigue": lambda a: a.fatigue,
                "Competence_Level": lambda a: a.competence_level,
                "Role_Clarity": lambda a: a.role_clarity,
                "Reporting_Threshold": lambda a: a.reporting_threshold,
                "MM_Team": lambda a: a.mental_model.values[0],
                "MM_Task": lambda a: a.mental_model.values[1],
                "MM_Process": lambda a: a.mental_model.values[2],
                "MM_Situation": lambda a: a.mental_model.values[3],
                "MM_Competence": lambda a: a.mental_model.values[4],
                "Info_Team": lambda a: a.information[0],
                "Info_Task": lambda a: a.information[1],
                "Info_Process": lambda a: a.information[2],
                "Info_Situation": lambda a: a.information[3],
                "Info_Competence": lambda a: a.information[4],
                "Delta_SA": lambda a: a.sa.sa - a.initial_sa,
                "Scenario_Components": lambda a: len(a.scenario_components)
            },
            model_reporters={
                "Avg_SA": lambda m: np.mean([a.sa.sa for a in m.schedule.agents]),
                "SA_Director": lambda m: np.mean([a.sa.sa for a in m.schedule.agents if a.role == "Director"]),
                "SA_Manager": lambda m: np.mean([a.sa.sa for a in m.schedule.agents if a.role == "Manager"]),
                "SA_Worker": lambda m: np.mean([a.sa.sa for a in m.schedule.agents if a.role == "Worker"])
            }
        )

    def get_communication_partners(self, agent):
        # Phase 3: Trust-driven and competence-based partner selection
        partners = []
        for other_agent in self.schedule.agents:
            if other_agent != agent:
                trust_weight = agent.trust.get(other_agent.unique_id, 0.5)
                structure_weight = self.org_structure[agent.unique_id, other_agent.unique_id]
                competence_weight = other_agent.competence_level
                total_weight = trust_weight * structure_weight * competence_weight
                if np.random.random() < total_weight:
                    partners.append(other_agent)
        return partners

    def update_communication_structure(self):
        # Phase 3: Update org_structure based on trust and competence
        for i, agent in enumerate(self.schedule.agents):
            for j, other_agent in enumerate(self.schedule.agents):
                if i != j:
                    trust = agent.trust.get(other_agent.unique_id, 0.5)
                    competence = other_agent.competence_level
                    self.org_structure[i, j] = min(1.0, self.org_structure[i, j] * (trust * competence))

    def step(self):
        self.step_count += 1
        self.datacollector.collect(self)
        self.schedule.step()
        self.update_communication_structure()  # Phase 3: Dynamic structure update
        try:
            agent_data = self.datacollector.get_agent_vars_dataframe()
            if not agent_data.empty and self.step_count > 1:
                current_step_data = agent_data.xs(self.step_count - 1, level="Step")
                self.avg_sa_change = np.mean(current_step_data["Delta_SA"])
        except (KeyError, IndexError):
            self.avg_sa_change = 0.0

def perform_statistical_tests(scenario_data):
    stats_results = []
    for role in ["All", "Director", "Manager", "Worker"]:
        role_data = {}
        sample_sizes = {}
        for scenario in SCENARIOS:
            df = scenario_data[scenario]
            final_step = df[df["Step"] == NUM_STEPS - 1]
            if role != "All":
                final_step = final_step[final_step["Role"] == role]
            iteration_means = final_step.groupby("Iteration")["SA"].mean().values
            role_data[scenario] = iteration_means
            sample_sizes[scenario] = len(iteration_means)
        f_stat, p_value = stats.f_oneway(*[role_data[s] for s in SCENARIOS])
        n_total = sum(sample_sizes.values())
        grand_mean = np.mean(np.concatenate([role_data[s] for s in SCENARIOS]))
        ss_between = sum(sample_sizes[s] * (np.mean(role_data[s]) - grand_mean)**2 for s in SCENARIOS)
        ss_total = sum(np.sum((role_data[s] - grand_mean)**2) for s in SCENARIOS)
        eta_squared = ss_between / ss_total if ss_total > 0 else 0
        stats_results.append({
            "Role": role,
            "Test": "ANOVA",
            "F_Statistic": f_stat,
            "P_Value": p_value,
            "Eta_Squared": eta_squared,
            "Significant": "Yes" if p_value < 0.05 else "No"
        })
        pairs = list(itertools.combinations(SCENARIOS.keys(), 2))
        for s1, s2 in pairs:
            t_stat, p_value = stats.ttest_ind(role_data[s1], role_data[s2], equal_var=False)
            adjusted_p = min(p_value * len(pairs), 1.0)
            n1, n2 = len(role_data[s1]), len(role_data[s2])
            s1_var, s2_var = np.var(role_data[s1], ddof=1), np.var(role_data[s2], ddof=1)
            pooled_std = np.sqrt(((n1-1)*s1_var + (n2-1)*s2_var) / (n1+n2-2))
            cohens_d = (np.mean(role_data[s1]) - np.mean(role_data[s2])) / pooled_std if pooled_std > 0 else 0
            se_diff = pooled_std * np.sqrt(1/n1 + 1/n2)
            mean_diff = np.mean(role_data[s1]) - np.mean(role_data[s2])
            t_critical = stats.t.ppf(0.975, n1+n2-2)
            ci_lower = mean_diff - t_critical * se_diff
            ci_upper = mean_diff + t_critical * se_diff
            stats_results.append({
                "Role": role,
                "Test": f"t-test (Scenario {s1} vs {s2})",
                "T_Statistic": t_stat,
                "P_Value": adjusted_p,
                "Cohens_D": cohens_d,
                "Mean_Diff": mean_diff,
                "CI_Lower": ci_lower,
                "CI_Upper": ci_upper,
                "Significant": "Yes" if adjusted_p < 0.05 else "No"
            })
    return pd.DataFrame(stats_results)

if __name__ == "__main__":
    scenario_data = {s: None for s in SCENARIOS}
    summary_data = []

    print("Starting Enhanced Mathematical SA Simulation with Dynamic Trust and Communication...")
    print(f"Scenarios: {list(SCENARIOS.keys())}")
    print(f"Iterations per scenario: {NUM_ITERATIONS}")
    print(f"Steps per iteration: {NUM_STEPS}")
    
    for scenario in SCENARIOS:
        print(f"\n{'='*50}")
        print(f"Running Scenario {scenario}")
        print(f"Components: {SCENARIOS[scenario]}")
        print(f"{'='*50}")
        
        iteration_dfs = []
        scenario_sa_changes = []
        
        for iteration in range(NUM_ITERATIONS):
            if iteration % 50 == 0:
                print(f"  Progress: {iteration}/{NUM_ITERATIONS} iterations")
                
            model = OrgModel(scenario)
            all_data = []

            for step in range(NUM_STEPS):
                model.step()
                try:
                    agent_data = model.datacollector.get_agent_vars_dataframe().xs(step, level="Step")
                    agent_data = agent_data.reset_index()
                    agent_data["Step"] = step
                    agent_data["Iteration"] = iteration
                    agent_data["Scenario"] = scenario
                    all_data.append(agent_data)
                except:
                    continue

            if all_data:
                iteration_df = pd.concat(all_data, ignore_index=True)
                iteration_dfs.append(iteration_df)
                final_step = iteration_df[iteration_df["Step"] == NUM_STEPS - 1]
                if not final_step.empty:
                    delta_sa = final_step.groupby("AgentID")["Delta_SA"].last()
                    avg_delta_sa = np.mean(delta_sa)
                    scenario_sa_changes.append(avg_delta_sa)
                    directors = final_step[final_step["Role"] == "Director"]["AgentID"]
                    managers = final_step[final_step["Role"] == "Manager"]["AgentID"]
                    workers = final_step[final_step["Role"] == "Worker"]["AgentID"]
                    summary_data.append({
                        "Scenario": scenario,
                        "Iteration": iteration,
                        "Avg_SA_Change": avg_delta_sa,
                        "SA_Change_Directors": np.mean([delta_sa[aid] for aid in directors if aid in delta_sa.index]) if len(directors) > 0 else 0,
                        "SA_Change_Managers": np.mean([delta_sa[aid] for aid in managers if aid in delta_sa.index]) if len(managers) > 0 else 0,
                        "SA_Change_Workers": np.mean([delta_sa[aid] for aid in workers if aid in delta_sa.index]) if len(workers) > 0 else 0
                    })

        if iteration_dfs:
            scenario_data[scenario] = pd.concat(iteration_dfs, ignore_index=True)
            output_file = f"mathematical_sa_simulation_scenario_{scenario}.xlsx"
            scenario_data[scenario].to_excel(output_file, index=False, sheet_name=f"Scenario_{scenario}")
            print(f"  Scenario {scenario} completed")
            print(f"  Mean SA change: {np.mean(scenario_sa_changes):.4f} ± {np.std(scenario_sa_changes):.4f}")
            print(f"  Data saved to: {output_file}")

    print(f"\n{'='*60}")
    print("PERFORMING STATISTICAL ANALYSIS")
    print(f"{'='*60}")
    
    stats_df = perform_statistical_tests(scenario_data)
    summary_df = pd.DataFrame(summary_data)
    
    with pd.ExcelWriter("mathematical_sa_simulation_summary.xlsx") as writer:
        summary_df.to_excel(writer, index=False, sheet_name="Summary")
        stats_df.to_excel(writer, index=False, sheet_name="Statistical_Tests")
        scenario_stats = summary_df.groupby('Scenario').agg({
            'Avg_SA_Change': ['mean', 'std', 'count', 'sem'],
            'SA_Change_Directors': ['mean', 'std'],
            'SA_Change_Managers': ['mean', 'std'],
            'SA_Change_Workers': ['mean', 'std']
        }).round(6)
        scenario_stats.to_excel(writer, sheet_name="Scenario_Statistics")
    
    print("\nSCENARIO PERFORMANCE COMPARISON:")
    print("-" * 60)
    scenario_means = summary_df.groupby('Scenario').agg({
        'Avg_SA_Change': ['mean', 'std', 'count']
    })['Avg_SA_Change']
    
    for scenario in SCENARIOS:
        if scenario in scenario_means.index:
            mean_val = scenario_means.loc[scenario, 'mean']
            std_val = scenario_means.loc[scenario, 'std']
            count_val = scenario_means.loc[scenario, 'count']
            se_val = std_val / np.sqrt(count_val)
            ci_95 = 1.96 * se_val
            print(f"Scenario {scenario}: {mean_val:.6f} ± {std_val:.6f} (95% CI: ±{ci_95:.6f})")
            print(f"  Components: {SCENARIOS[scenario]}")
            print(f"  Sample size: {int(count_val)}")
            print()
    
    print("\nSTATISTICAL SIGNIFICANCE RESULTS:")
    print("=" * 60)
    
    for role in ["All", "Director", "Manager", "Worker"]:
        print(f"\n{role.upper()} ROLE ANALYSIS:")
        print("-" * 40)
        anova_result = stats_df[(stats_df["Role"] == role) & (stats_df["Test"] == "ANOVA")]
        if not anova_result.empty:
            f_stat = anova_result['F_Statistic'].iloc[0]
            p_val = anova_result['P_Value'].iloc[0]
            eta_sq = anova_result['Eta_Squared'].iloc[0]
            significant = anova_result['Significant'].iloc[0]
            print(f"ANOVA: F({len(SCENARIOS)-1}, {NUM_ITERATIONS*len(SCENARIOS)-len(SCENARIOS)}) = {f_stat:.4f}")
            print(f"       p = {p_val:.6f} [{significant}]")
            print(f"       η² = {eta_sq:.4f} ({'Large' if eta_sq > 0.14 else 'Medium' if eta_sq > 0.06 else 'Small'} effect)")
        pairwise_tests = stats_df[(stats_df["Role"] == role) & (stats_df["Test"].str.contains("t-test"))]
        if not pairwise_tests.empty:
            print("\nPairwise Comparisons (Bonferroni corrected):")
            for _, row in pairwise_tests.iterrows():
                comparison = row['Test'].replace('t-test ', '').replace('(', '').replace(')', '')
                t_stat = row['T_Statistic']
                p_val = row['P_Value']
                cohens_d = row['Cohens_D']
                mean_diff = row['Mean_Diff']
                ci_lower = row['CI_Lower']
                ci_upper = row['CI_Upper']
                significant = row['Significant']
                effect_size = 'Large' if abs(cohens_d) > 0.8 else 'Medium' if abs(cohens_d) > 0.5 else 'Small'
                print(f"  {comparison}:")
                print(f"    t = {t_stat:.4f}, p = {p_val:.6f} [{significant}]")
                print(f"    Mean difference = {mean_diff:.6f}")
                print(f"    95% CI: [{ci_lower:.6f}, {ci_upper:.6f}]")
                print(f"    Cohen's d = {cohens_d:.4f} ({effect_size} effect)")
                print()

    significant_results = stats_df[stats_df['Significant'] == 'Yes']
    total_tests = len(stats_df)
    significant_count = len(significant_results)
    
    print(f"\nSUMMARY:")
    print("=" * 30)
    print(f"Total statistical tests performed: {total_tests}")
    print(f"Statistically significant results: {significant_count}")
    print(f"Percentage significant: {(significant_count/total_tests)*100:.1f}%")
    
    if significant_count > 0:
        print(f"\nSignificant findings:")
        for _, row in significant_results.iterrows():
            role = row['Role']
            test = row['Test']
            p_val = row['P_Value']
            if 'F_Statistic' in row:
                print(f"  {role} - {test}: F = {row['F_Statistic']:.4f}, p = {p_val:.6f}")
            else:
                print(f"  {role} - {test}: t = {row['T_Statistic']:.4f}, p = {p_val:.6f}")
    
    print(f"\nDynamic trust and communication simulation completed.")
    print(f"Results saved to 'mathematical_sa_simulation_summary.xlsx'")
    
    print(f"\nTHEORETICAL PREDICTIONS:")
    print("-" * 30)
    print("Based on enhanced mathematical formulation, expected SA ranking:")
    print("1. Scenario 3 (Highest - P+C+J with synergies and dynamic trust)")
    print("2. Scenario 2 (High - P+C with adaptive communication)")
    print("3. Scenario 4 (Variable - Role-dependent complexity with dynamic authority)")
    print("4. Scenario 1 (Baseline - P only with static structure)")
    
    print(f"\nACTUAL RESULTS (mean SA change):")
    print("-" * 30)
    actual_means = []
    for scenario in SCENARIOS:
        if scenario in scenario_means.index:
            mean_val = scenario_means.loc[scenario, 'mean']
            actual_means.append((scenario, mean_val))
    
    actual_means.sort(key=lambda x: x[1], reverse=True)
    for i, (scenario, mean_val) in enumerate(actual_means, 1):
        components = SCENARIOS[scenario]
        comp_str = "+".join([list(components[role])[0] if len(set().union(*components.values())) == 1 
                           else "+".join(sorted(set().union(*components.values()))) 
                           for role in components][0:1])
        if len(set().union(*components.values())) > 1:
            comp_str = "+".join(sorted(set().union(*components.values())))
        print(f"{i}. Scenario {scenario}: {mean_val:.6f} ({comp_str})")
    
    print(f"\n" + "="*60)
    print("DYNAMIC TRUST AND COMMUNICATION SIMULATION COMPLETED")
    print("="*60)
