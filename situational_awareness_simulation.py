import numpy as np
import pandas as pd
from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.datacollection import DataCollector
import uuid

# Constants
NUM_DIRECTORS = 3
NUM_MANAGERS = 7
NUM_WORKERS = 20
NUM_AGENTS = NUM_DIRECTORS + NUM_MANAGERS + NUM_WORKERS
NUM_STEPS = 100
REPORTING_THRESHOLD = {"Worker": 0.3, "Manager": 0.5, "Director": 0.7}
NOISE_STD = {"reporting": 0.1, "communication": 0.05, "mental_model": 0.05}
LEARNING_RATE = 0.1
SA_WEIGHTS = {"perception": 0.4, "comprehension": 0.3, "projection": 0.3}

def sigmoid(x):
    """Sigmoid function for normalizing values."""
    return 1 / (1 + np.exp(-x))

class MentalModel:
    """Manages the 5D mental model of an agent."""
    def __init__(self):
        # Initialize mental model: [team, task, process, situation, competence]
        self.values = np.random.uniform(0.3, 0.7, 5)

    def update(self, delta, noise_std=NOISE_STD["mental_model"]):
        """Update mental model with adjustment and noise."""
        noise = np.random.normal(0, noise_std, 5)
        self.values = np.clip(self.values + LEARNING_RATE * delta + noise, 0, 1)

    def cosine_similarity(self, other_model):
        """Compute cosine similarity with another mental model."""
        norm = np.linalg.norm(self.values) * np.linalg.norm(other_model)
        return np.dot(self.values, other_model) / norm if norm != 0 else 0

class SituationalAwareness:
    """Manages SA components: perception, comprehension, projection."""
    def __init__(self):
        self.perception = 0.0
        self.comprehension = 0.0
        self.projection = 0.0
        self.sa = np.random.uniform(0.2, 0.5)  # Overall SA level
        self.previous_sa = self.sa

    def update(self, perception, comprehension, projection):
        """Update SA based on Endsley's model."""
        self.perception = perception
        self.comprehension = comprehension
        self.projection = projection
        self.previous_sa = self.sa
        self.sa = (SA_WEIGHTS["perception"] * perception +
                   SA_WEIGHTS["comprehension"] * comprehension +
                   SA_WEIGHTS["projection"] * projection)
        self.sa = np.clip(self.sa, 0, 1)

class Communication:
    """Handles reporting and message passing with noise."""
    def __init__(self, role, communication_prob):
        self.role = role
        self.communication_prob = communication_prob
        self.messages = []

    def generate_report(self, information, sa, trust):
        """Generate report if SA exceeds threshold and random check passes."""
        if sa >= REPORTING_THRESHOLD[self.role] and np.random.random() < self.communication_prob:
            noise = np.random.normal(0, NOISE_STD["reporting"], 5)
            report = information * sa * trust + noise
            return np.clip(report, 0, 1)
        return None

    def receive_message(self, message):
        """Store incoming message with communication noise."""
        if message is not None:
            noise = np.random.normal(0, NOISE_STD["communication"], 5)
            self.messages.append(np.clip(message + noise, 0, 1))

class OrgAgent(Agent):
    """Agent with role, mental model, SA, and communication."""
    def __init__(self, unique_id, model, role):
        super().__init__(unique_id, model)
        self.role = role
        self.trust = np.random.uniform(0.5, 1.0)
        self.communication_prob = np.random.uniform(0.6, 0.9)
        self.task_familiarity = np.random.uniform(0.3, 0.9)
        self.process_understanding = np.random.uniform(0.3, 0.9)
        self.competence_level = np.random.uniform(0.4, 0.9)
        self.mental_model = MentalModel()
        self.sa = SituationalAwareness()
        self.communication = Communication(role, self.communication_prob)
        self.information = np.random.uniform(0, 1, 5)  # Information state
        self.initial_sa = self.sa.sa  # For delta SA calculation

    def perceive(self):
        """Calculate perception based on task familiarity and complexity."""
        task_complexity = self.model.task_complexity
        self.sa.perception = sigmoid(self.task_familiarity - task_complexity + np.random.normal(0, NOISE_STD["mental_model"]))

    def comprehend(self):
        """Calculate comprehension based on perception and process understanding."""
        self.sa.comprehension = sigmoid(self.sa.perception * self.process_understanding + np.random.normal(0, NOISE_STD["mental_model"]))

    def project(self):
        """Calculate projection based on comprehension and competence."""
        self.sa.projection = sigmoid(self.sa.comprehension * self.competence_level + np.random.normal(0, NOISE_STD["mental_model"]))
        # Update projection to reflect expected SA change
        self.sa.projection += self.sa.sa - self.sa.previous_sa

    def communicate(self):
        """Communicate with partners based on organizational structure."""
        report = self.communication.generate_report(self.information, self.sa.sa, self.trust)
        if report is not None:
            partners = self.model.get_communication_partners(self)
            for partner in partners:
                partner.communication.receive_message(report)

    def update_mental_model(self):
        """Update mental model based on received messages."""
        if self.communication.messages:
            avg_message = np.mean(self.communication.messages, axis=0)
            delta_mm = avg_message - self.mental_model.values
            self.mental_model.update(delta_mm)
            self.communication.messages = []

    def step(self):
        """First phase: Communicate with other agents."""
        self.communicate()

    def advance(self):
        """Second phase: Update SA and mental model."""
        self.perceive()
        self.comprehend()
        self.project()
        self.sa.update(self.sa.perception, self.sa.comprehension, self.sa.projection)
        self.update_mental_model()

    def get_data(self):
        """Return agent data for collection."""
        return {
            "Role": self.role,
            "SA": self.sa.sa,
            "SA_P": self.sa.perception,
            "SA_C": self.sa.comprehension,
            "SA_J": self.sa.projection,
            "Trust": self.trust,
            "Comm_Prob": self.communication_prob,
            "Task_Familiarity": self.task_familiarity,
            "Process_Understanding": self.process_understanding,
            "Competence_Level": self.competence_level,
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
            "Delta_SA": self.sa.sa - self.initial_sa
        }

class OrgModel(Model):
    """Mesa model for organizational SA simulation."""
    def __init__(self):
        self.num_agents = NUM_AGENTS
        self.schedule = SimultaneousActivation(self)
        self.task_complexity = np.random.uniform(0.4, 0.8)
        self.true_mental_model = np.ones(5) * 0.8
        self.true_information = np.ones(5) * 0.9

        # Organizational structure matrix
        self.org_structure = np.zeros((NUM_AGENTS, NUM_AGENTS))
        roles = ["Director"] * NUM_DIRECTORS + ["Manager"] * NUM_MANAGERS + ["Worker"] * NUM_WORKERS
        for i in range(NUM_AGENTS):
            for j in range(NUM_AGENTS):
                if i != j:
                    if (roles[i] == "Worker" and roles[j] == "Manager") or \
                       (roles[i] == "Manager" and roles[j] in ["Worker", "Director"]) or \
                       (roles[i] == "Director" and roles[j] == "Manager"):
                        self.org_structure[i, j] = 1

        # Create agents
        for i, role in enumerate(roles):
            agent = OrgAgent(i, self, role)
            self.schedule.add(agent)

        # Data collector
        self.datacollector = DataCollector(
            agent_reporters={
                "Role": lambda a: a.role,
                "SA": lambda a: a.sa.sa,
                "SA_P": lambda a: a.sa.perception,
                "SA_C": lambda a: a.sa.comprehension,
                "SA_J": lambda a: a.sa.projection,
                "Trust": lambda a: a.trust,
                "Comm_Prob": lambda a: a.communication_prob,
                "Task_Familiarity": lambda a: a.task_familiarity,
                "Process_Understanding": lambda a: a.process_understanding,
                "Competence_Level": lambda a: a.competence_level,
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
                "Delta_SA": lambda a: a.sa.sa - a.initial_sa
            },
            model_reporters={
                "Avg_SA": lambda m: np.mean([a.sa.sa for a in m.schedule.agents]),
                "SA_Director": lambda m: np.mean([a.sa.sa for a in m.schedule.agents if a.role == "Director"]),
                "SA_Manager": lambda m: np.mean([a.sa.sa for a in m.schedule.agents if a.role == "Manager"]),
                "SA_Worker": lambda m: np.mean([a.sa.sa for a in m.schedule.agents if a.role == "Worker"])
            }
        )

    def get_communication_partners(self, agent):
        """Return list of agents that the given agent can communicate with."""
        return [a for a in self.schedule.agents if self.org_structure[agent.unique_id, a.unique_id]]

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.schedule.step()

# Run the simulation and save results to Excel
if __name__ == "__main__":
    model = OrgModel()
    all_data = []

    # Run for NUM_STEPS and collect data
    for step in range(NUM_STEPS):
        model.step()
        agent_data = model.datacollector.get_agent_vars_dataframe().xs(step, level="Step")
        agent_data = agent_data.reset_index()
        agent_data["Step"] = step
        all_data.append(agent_data)

    # Combine all steps into a single DataFrame
    final_data = pd.concat(all_data, ignore_index=True)

    # Save to Excel
    output_file = "sa_simulation_results.xlsx"
    final_data.to_excel(output_file, index=False, sheet_name="Simulation_Data")

    # Print summary statistics
    final_step = final_data[final_data["Step"] == NUM_STEPS - 1]
    delta_sa = final_step.groupby("AgentID")["Delta_SA"].last()
    avg_delta_sa = np.mean(delta_sa)
    print(f"Average SA Change: {avg_delta_sa:.4f}")
    for role in ["Director", "Manager", "Worker"]:
        role_agent_ids = final_step[final_step["Role"] == role]["AgentID"]
        role_delta = np.mean([delta_sa[aid] for aid in role_agent_ids if aid in delta_sa])
        print(f"Average SA Change ({role}): {role_delta:.4f}")