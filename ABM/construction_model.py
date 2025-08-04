import mesa
import random
import numpy as np
import pandas as pd
from datetime import datetime, time
import os
import traceback
import logging
from typing import List, Dict
from filelock import FileLock, Timeout
from enums import ReportingStructure, OrgStructure, AgentRole, EventType, ActionType, ProjectPhase, Criticality
from data_classes import ProjectOutcomes

logging.basicConfig(filename='simulation_model.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionModel(mesa.Model):
    def __init__(
        self,
        width: int = 20,
        height: int = 20,
        reporting_structure: str = "self",
        org_structure: str = "functional",
        hazard_prob: float = 0.01,
        delay_prob: float = 0.015,
        resource_prob: float = 0.001,
        comm_failure_dedicated: float = 0.04,
        comm_failure_self: float = 0.05,
        comm_failure_none: float = 0.0,
        worker_detection: float = 0.80,
        manager_detection: float = 0.90,
        reporter_detection: float = 0.95,
        director_detection: float = 0.85,
        worker_reporting: float = 0.80,
        manager_reporting: float = 0.90,
        reporter_reporting: float = 0.95,
        director_reporting: float = 0.85,
        initial_budget: float = 1000000,
        initial_equipment: int = 500,
        run_id: int = 1
    ):
        super().__init__()
        self.width = width
        self.height = height
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.RandomActivation(self)
        self.reporting_structure = ReportingStructure(reporting_structure.lower())
        self.org_structure = OrgStructure(org_structure.lower())
        self.outcomes = ProjectOutcomes()
        self.reports = []
        self.current_events = []
        self.event_counts = {EventType.HAZARD: 0, EventType.DELAY: 0, EventType.RESOURCE_SHORTAGE: 0}
        self.base_hazard_prob = hazard_prob
        self.base_delay_prob = delay_prob
        self.resource_prob = resource_prob
        self.comm_failure_dedicated = comm_failure_dedicated
        self.comm_failure_self = comm_failure_self
        self.comm_failure_none = comm_failure_none
        self.worker_detection = worker_detection
        self.manager_detection = manager_detection
        self.reporter_detection = reporter_detection
        self.director_detection = director_detection
        self.worker_reporting = worker_reporting
        self.manager_reporting = manager_reporting
        self.reporter_reporting = reporter_reporting
        self.director_reporting = director_reporting
        self.budget = initial_budget
        self.equipment_available = initial_equipment
        self.organizational_memory = {
            EventType.HAZARD: [],
            EventType.DELAY: [],
            EventType.RESOURCE_SHORTAGE: []
        }
        self.previous_adherence = 0.0
        self.simulation_id = f"sim_{datetime.now().strftime('%Y%m%d_%H%M%S')}_run{run_id:03d}"
        self._initialized = False
        self.hazard_acted_this_step = False
        self.initial_sa_scores = {}
        self.project_phase = ProjectPhase.FOUNDATION  # Initialize project phase
        self.critical_tasks = set()  # Track critical path tasks
        self.supplier_communication = []  # Track supplier interactions
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "SafetyIncidents": lambda m: m.outcomes.safety_incidents,
                "IncidentPoints": lambda m: m.outcomes.incident_points,
                "ScheduleAdherence": lambda m: (
                    m.outcomes.tasks_completed_on_time / m.outcomes.total_tasks * 100
                    if m.outcomes.total_tasks > 0 else 0
                ),
                "CostOverruns": lambda m: m.outcomes.cost_overruns,
                "AverageSA": lambda m: np.mean([a.awareness.total_score() for a in m.schedule.agents]),
                "Worker_SA": lambda m: (
                    np.mean([a.awareness.total_score() for a in m.schedule.agents if a.role == AgentRole.WORKER])
                    if any(a.role == AgentRole.WORKER for a in m.schedule.agents) else 0
                ),
                "Manager_SA": lambda m: (
                    np.mean([a.awareness.total_score() for a in m.schedule.agents if a.role == AgentRole.MANAGER])
                    if any(a.role == AgentRole.MANAGER for a in m.schedule.agents) else 0
                ),
                "Director_SA": lambda m: (
                    np.mean([a.awareness.total_score() for a in m.schedule.agents if a.role == AgentRole.DIRECTOR])
                    if any(a.role == AgentRole.DIRECTOR for a in m.schedule.agents) else 0
                ),
                "Reporter_SA": lambda m: (
                    np.mean([a.awareness.total_score() for a in m.schedule.agents if a.role == AgentRole.REPORTER])
                    if any(a.role == AgentRole.REPORTER for a in m.schedule.agents) else 0
                ),
                "Worker_Reports_Sent": lambda m: (
                    np.sum([a.reports_sent for a in m.schedule.agents if a.role == AgentRole.WORKER])
                    if any(a.role == AgentRole.WORKER for a in m.schedule.agents) else 0
                ),
                "Manager_Reports_Sent": lambda m: (
                    np.sum([a.reports_sent for a in m.schedule.agents if a.role == AgentRole.MANAGER])
                    if any(a.role == AgentRole.MANAGER for a in m.schedule.agents) else 0
                ),
                "Director_Reports_Sent": lambda m: (
                    np.sum([a.reports_sent for a in m.schedule.agents if a.role == AgentRole.DIRECTOR])
                    if any(a.role == AgentRole.DIRECTOR for a in m.schedule.agents) else 0
                ),
                "Reporter_Reports_Sent": lambda m: (
                    np.sum([a.reports_sent for a in m.schedule.agents if a.role == AgentRole.REPORTER])
                    if any(a.role == AgentRole.REPORTER for a in m.schedule.agents) else 0
                ),
                "Worker_Reports_Received": lambda m: (
                    np.sum([len(a.reports_received) for a in m.schedule.agents if a.role == AgentRole.WORKER])
                    if any(a.role == AgentRole.WORKER for a in m.schedule.agents) else 0
                ),
                "Manager_Reports_Received": lambda m: (
                    np.sum([len(a.reports_received) for a in m.schedule.agents if a.role == AgentRole.MANAGER])
                    if any(a.role == AgentRole.MANAGER for a in m.schedule.agents) else 0
                ),
                "Director_Reports_Received": lambda m: (
                    np.sum([len(a.reports_received) for a in m.schedule.agents if a.role == AgentRole.DIRECTOR])
                    if any(a.role == AgentRole.DIRECTOR for a in m.schedule.agents) else 0
                ),
                "Reporter_Reports_Received": lambda m: (
                    np.sum([len(a.reports_received) for a in m.schedule.agents if a.role == AgentRole.REPORTER])
                    if any(a.role == AgentRole.REPORTER for a in m.schedule.agents) else 0
                ),
                "TotalTasks": lambda m: m.outcomes.total_tasks,
                "TasksCompletedOnTime": lambda m: m.outcomes.tasks_completed_on_time,
                "BudgetRemaining": lambda m: m.budget,
                "EquipmentAvailable": lambda m: m.equipment_available,
                "Worker_Act_Count": lambda m: (
                    np.sum([a.actions_taken[ActionType.ACT] for a in m.schedule.agents if a.role == AgentRole.WORKER])
                    if any(a.role == AgentRole.WORKER for a in m.schedule.agents) else 0
                ),
                "Manager_Act_Count": lambda m: (
                    np.sum([a.actions_taken[ActionType.ACT] for a in m.schedule.agents if a.role == AgentRole.MANAGER])
                    if any(a.role == AgentRole.MANAGER for a in m.schedule.agents) else 0
                ),
                "Director_Act_Count": lambda m: (
                    np.sum([a.actions_taken[ActionType.ACT] for a in m.schedule.agents if a.role == AgentRole.DIRECTOR])
                    if any(a.role == AgentRole.DIRECTOR for a in m.schedule.agents) else 0
                ),
                "Reporter_Act_Count": lambda m: (
                    np.sum([a.actions_taken[ActionType.ACT] for a in m.schedule.agents if a.role == AgentRole.REPORTER])
                    if any(a.role == AgentRole.REPORTER for a in m.schedule.agents) else 0
                ),
                "ProjectPhase": lambda m: m.project_phase.value,
                "CriticalTasks": lambda m: len(m.critical_tasks),
                "SupplierCommunications": lambda m: len(m.supplier_communication)
            },
            agent_reporters={
                "Role": lambda a: a.role.value,
                "SA_Score": lambda a: a.awareness.total_score(),
                "SA_Level": lambda a: a.awareness.total_score() - self.initial_sa_scores.get(a.unique_id, 0),
                "ReportsSent": lambda a: a.reports_sent,
                "Workload": lambda a: a.workload,
                "Fatigue": lambda a: a.fatigue,
                "Experience": lambda a: a.experience,
                "RiskTolerance": lambda a: a.risk_tolerance
            }
        )
        self.metrics_log = []
        self.agent_sa_log = []
        self.configuration_log = []

        if not self._initialized:
            self.log_configuration()
            self.setup_excel_logging()
            self.initialize_agents()
            self._initialized = True
            logging.debug(f"Model initialized with simulation_id: {self.simulation_id}, excel_filepath: {self.excel_filepath}")
        else:
            logging.warning(f"Model reinitialization attempted for simulation_id: {self.simulation_id}")

    def setup_excel_logging(self):
        output_dir = os.path.join(os.getcwd(), "simulation_outputs")
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
                logging.debug(f"Created output directory: {output_dir}")
            except Exception as e:
                print(f"Failed to create output directory {output_dir}: {e}")
                logging.error(f"Directory creation error: {traceback.format_exc()}")

        filename = f"construction_simulation_{self.simulation_id}.xlsx"
        self.excel_filepath = os.path.join(output_dir, filename)
        self.csv_filepath = os.path.join(output_dir, filename.replace('.xlsx', '.csv'))
        self.lock_filepath = self.excel_filepath + ".lock"

        try:
            with FileLock(self.lock_filepath, timeout=30):
                with pd.ExcelWriter(self.excel_filepath, engine='openpyxl', mode='w') as writer:
                    pd.DataFrame(self.configuration_log).to_excel(writer, sheet_name='Configuration', index=False)
                logging.debug(f"Initialized new Excel file: {self.excel_filepath}")
        except Timeout as e:
            print(f"Timeout initializing Excel file {self.excel_filepath}: {e}")
            logging.error(f"Excel initialization timeout: {traceback.format_exc()}")
            if self.configuration_log:
                pd.DataFrame(self.configuration_log).to_csv(self.csv_filepath, index=False)
                logging.debug(f"Configuration saved to fallback CSV: {self.csv_filepath}")
        except Exception as e:
            print(f"Error initializing Excel file {self.excel_filepath}: {e}")
            logging.error(f"Excel initialization error: {traceback.format_exc()}")
            if self.configuration_log:
                pd.DataFrame(self.configuration_log).to_csv(self.csv_filepath, index=False)
                logging.debug(f"Configuration saved to fallback CSV: {self.csv_filepath}")

    def get_current_comm_failure(self):
        base_comm_failure = (
            self.comm_failure_dedicated if self.reporting_structure == ReportingStructure.DEDICATED else
            self.comm_failure_self if self.reporting_structure == ReportingStructure.SELF else
            self.comm_failure_none
        )
        if self.outcomes.safety_incidents > 5:
            base_comm_failure *= 1.3
        if self.org_structure == OrgStructure.FLAT:
            return base_comm_failure * 0.8
        elif self.org_structure == OrgStructure.HIERARCHICAL:
            return base_comm_failure * 1.2
        return base_comm_failure

    def log_configuration(self):
        config_data = {
            "Simulation_ID": self.simulation_id,
            "Step": 0,
            "Reporting_Structure": self.reporting_structure.value,
            "Org_Structure": self.org_structure.value,
            "Hazard_Probability": self.base_hazard_prob,
            "Delay_Probability": self.base_delay_prob,
            "Resource_Shortage_Probability": self.resource_prob,
            "Comm_Failure_Dedicated": self.comm_failure_dedicated,
            "Comm_Failure_Self": self.comm_failure_self,
            "Comm_Failure_None": self.comm_failure_none,
            "Worker_Detection": self.worker_detection,
            "Manager_Detection": self.manager_detection,
            "Reporter_Detection": self.reporter_detection,
            "Director_Detection": self.director_detection,
            "Worker_Reporting": self.worker_reporting,
            "Manager_Reporting": self.manager_reporting,
            "Reporter_Reporting": self.reporter_reporting,
            "Director_Reporting": self.director_reporting,
            "Initial_Budget": self.budget,
            "Initial_Equipment": self.equipment_available,
            "Grid_Width": self.width,
            "Grid_Height": self.height,
            "Project_Phase": self.project_phase.value,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.configuration_log = [config_data]
        logging.debug(f"Configuration logged for simulation_id: {self.simulation_id}")

    def initialize_agents(self):
        from construction_agent import ConstructionAgent
        for agent in self.schedule.agents[:]:
            self.schedule.remove(agent)
            self.grid.remove_agent(agent)

        agent_id = 0
        worker_count = 50
        manager_count = 10 if self.org_structure != OrgStructure.FLAT else 5
        director_count = 3 if self.org_structure != OrgStructure.FLAT else 1
        reporter_count = 5 if self.reporting_structure == ReportingStructure.DEDICATED else 0
        for _ in range(worker_count):
            pos = (random.randrange(self.width), random.randrange(self.height))
            agent = ConstructionAgent(agent_id, self, AgentRole.WORKER, pos)
            self.schedule.add(agent)
            self.grid.place_agent(agent, pos)
            agent_id += 1
        for _ in range(manager_count):
            pos = (random.randrange(self.width), random.randrange(self.height))
            agent = ConstructionAgent(agent_id, self, AgentRole.MANAGER, pos)
            self.schedule.add(agent)
            self.grid.place_agent(agent, pos)
            agent_id += 1
        for _ in range(director_count):
            pos = (random.randrange(self.width), random.randrange(self.height))
            agent = ConstructionAgent(agent_id, self, AgentRole.DIRECTOR, pos)
            self.schedule.add(agent)
            self.grid.place_agent(agent, pos)
            agent_id += 1
        for _ in range(reporter_count):
            pos = (random.randrange(self.width), random.randrange(self.height))
            agent = ConstructionAgent(agent_id, self, AgentRole.REPORTER, pos)
            self.schedule.add(agent)
            self.grid.place_agent(agent, pos)
            agent_id += 1
        self.log_agent_situational_awareness()

    def update_project_phase(self):
        # Update project phase based on simulation progress
        total_steps = 100  # Assuming 100 steps as per main.py
        current_step = self.schedule.steps
        if current_step < 33:
            self.project_phase = ProjectPhase.FOUNDATION
        elif current_step < 66:
            self.project_phase = ProjectPhase.FRAMING
        else:
            self.project_phase = ProjectPhase.INTERIOR
        logging.debug(f"Step {current_step}: Project phase updated to {self.project_phase.value}")

    def get_events(self) -> List[Dict]:
        self.current_events = []
        self.outcomes.total_tasks_added_this_step = False
        self.hazard_acted_this_step = False
        worker_fatigue = (
            np.mean([a.fatigue for a in self.schedule.agents if a.role == AgentRole.WORKER])
            if any(a.role == AgentRole.WORKER for a in self.schedule.agents) else 0.5
        )
        budget_factor = max(0.1, 1 - self.budget / 1000000)
        org_factor = 0.8 if self.org_structure == OrgStructure.FLAT else 1.0
        incident_factor = min(1.0, 1 + 0.05 * self.outcomes.safety_incidents)
        phase_factor = 1.5 if self.project_phase == ProjectPhase.FOUNDATION else 1.0
        hazard_prob = self.base_hazard_prob * (1 + 0.3 * worker_fatigue) * (1 + 0.5 * budget_factor) * org_factor * incident_factor * phase_factor
        hazard_prob = min(hazard_prob, 0.4)
        delay_prob = self.base_delay_prob * (1 + 0.01 * budget_factor) * phase_factor
        effective_resource_prob = self.resource_prob

        if random.random() < hazard_prob:
            severity = random.uniform(0.5, 1.0)
            criticality = Criticality.CRITICAL if severity > 0.8 and self.project_phase == ProjectPhase.FOUNDATION else Criticality.NON_CRITICAL
            event = {"type": EventType.HAZARD, "description": "Loose scaffold", "severity": severity, "criticality": criticality}
            self.current_events.append(event)
            self.event_counts[EventType.HAZARD] += 1
            delay_prob += 0.05 * severity
            effective_resource_prob += 0.03 * severity
            if criticality == Criticality.CRITICAL:
                self.critical_tasks.add(len(self.current_events) - 1)
            logging.info(
                f"Generated HAZARD event at step {self.schedule.steps}, "
                f"severity={severity:.2f}, criticality={criticality.value}, prob={hazard_prob:.3f}, event_count={self.event_counts[EventType.HAZARD]}"
            )

        if random.random() < delay_prob and not self.outcomes.total_tasks_added_this_step:
            severity = random.uniform(0.3, 0.7)
            criticality = Criticality.CRITICAL if self.project_phase == ProjectPhase.FOUNDATION else Criticality.NON_CRITICAL
            event = {"type": EventType.DELAY, "description": "Supply chain delay", "severity": severity, "criticality": criticality}
            self.current_events.append(event)
            self.event_counts[EventType.DELAY] += 1
            self.outcomes.total_tasks += 1
            self.outcomes.total_tasks_added_this_step = True
            effective_resource_prob += 0.02 * severity
            if criticality == Criticality.CRITICAL:
                self.critical_tasks.add(len(self.current_events) - 1)
            logging.info(
                f"Generated DELAY event at step {self.schedule.steps}, "
                f"severity={severity:.2f}, criticality={criticality.value}, prob={delay_prob:.3f}, Total Tasks={self.outcomes.total_tasks}"
            )

        if random.random() < effective_resource_prob:
            severity = random.uniform(0.2, 0.5)
            criticality = Criticality.NON_CRITICAL
            event = {"type": EventType.RESOURCE_SHORTAGE, "description": "Material unavailability", "severity": severity, "criticality": criticality}
            self.current_events.append(event)
            self.event_counts[EventType.RESOURCE_SHORTAGE] += 1
            self.supplier_communication.append({"step": self.schedule.steps, "event": event})
            logging.info(
                f"Generated RESOURCE_SHORTAGE event at step {self.schedule.steps}, "
                f"severity={severity:.2f}, criticality={criticality.value}, prob={effective_resource_prob:.3f}"
            )

        if not self.current_events:
            logging.info(f"No events generated at step {self.schedule.steps}")
        else:
            logging.info(
                f"Generated events at step {self.schedule.steps}: "
                f"{[event['type'].value for event in self.current_events]}"
            )
        return self.current_events if self.current_events else [None]

    def send_report(self, sender, report: Dict) -> bool:
        self.reports.append(report)
        comm_failure = self.get_current_comm_failure()
        success = False
        event = report.get("event")
        comm_radius = 5 if self.org_structure == OrgStructure.FLAT else 3 if self.org_structure == OrgStructure.FUNCTIONAL else 2
        regulatory_required = event.get("type") == EventType.HAZARD and event.get("severity", 0) >= 0.5

        if self.reporting_structure == ReportingStructure.DEDICATED:
            if sender.role != AgentRole.REPORTER:
                neighbors = self.grid.get_neighbors(sender.pos, moore=True, include_center=False, radius=comm_radius)
                for agent in self.schedule.agents:
                    if agent in neighbors and agent.role == AgentRole.REPORTER and random.random() > comm_failure:
                        agent.reports_received.append(report)
                        success = True
                        severity = report.get("event", {}).get("severity", 0)
                        report["event"]["severity"] = min(severity * 1.1, 1.0)
                        logging.info(
                            f"Step {self.schedule.steps}: {sender.role.value} {sender.unique_id} sent to "
                            f"REPORTER {agent.unique_id}, event={event.get('type').value}"
                        )
                if self.org_structure == OrgStructure.FUNCTIONAL or regulatory_required:
                    target_roles = []
                    if sender.role == AgentRole.WORKER:
                        target_roles = [AgentRole.MANAGER]
                    elif sender.role == AgentRole.MANAGER:
                        target_roles = [AgentRole.DIRECTOR]
                    elif sender.role == AgentRole.DIRECTOR:
                        target_roles = [AgentRole.MANAGER]
                    for agent in self.schedule.agents:
                        if agent != sender and agent.role in target_roles and agent in neighbors and random.random() > comm_failure:
                            agent.reports_received.append(report)
                            success = True
                            if event and not report.get("acted_on", False):
                                follow_up_action = agent.decide_action(event, is_follow_up=True)
                                agent.execute_action(event, follow_up_action)
                                report["acted_on"] = True
                                logging.info(
                                    f"Step {self.schedule.steps}: {sender.role.value} {sender.unique_id} sent to "
                                    f"{agent.role.value} {agent.unique_id}, action={follow_up_action.value}, "
                                    f"event={event.get('type').value}"
                                )
            else:
                aggregated_report = {"type": "AGGREGATED", "events": [], "acted_on": False}
                for r in sender.reports_received:
                    event = r.get("event", {})
                    if event and event.get("type"):
                        existing = next((e for e in aggregated_report["events"] if e["type"] == event["type"]), None)
                        if existing:
                            existing["severity"] = max(existing["severity"], event["severity"])
                        else:
                            aggregated_report["events"].append({
                                "type": event["type"],
                                "severity": event["severity"],
                                "description": event["description"],
                                "criticality": event["criticality"]
                            })
                if aggregated_report["events"]:
                    for agent in self.schedule.agents:
                        if agent.role != AgentRole.REPORTER and random.random() > comm_failure:
                            agent.reports_received.append(aggregated_report)
                            success = True
                            if not aggregated_report["acted_on"]:
                                for event in aggregated_report["events"]:
                                    follow_up_action = agent.decide_action(event, is_follow_up=True)
                                    agent.execute_action(event, follow_up_action)
                                aggregated_report["acted_on"] = True
                            logging.info(
                                f"Step {self.schedule.steps}: REPORTER {sender.unique_id} broadcast aggregated report "
                                f"to {agent.role.value} {agent.unique_id}, events={[e['type'].value for e in aggregated_report['events']]}"
                            )
        elif self.reporting_structure == ReportingStructure.SELF:
            neighbors = self.grid.get_neighbors(sender.pos, moore=True, include_center=False, radius=comm_radius)
            target_roles = []
            if self.org_structure == OrgStructure.FUNCTIONAL or regulatory_required:
                if sender.role == AgentRole.WORKER:
                    target_roles = [AgentRole.MANAGER]
                elif sender.role == AgentRole.MANAGER:
                    target_roles = [AgentRole.DIRECTOR]
                elif sender.role == AgentRole.DIRECTOR:
                    target_roles = [AgentRole.MANAGER]
            else:
                target_roles = [AgentRole.WORKER, AgentRole.MANAGER, AgentRole.DIRECTOR]
            for agent in self.schedule.agents:
                if agent != sender and agent.role in target_roles and agent in neighbors and random.random() > comm_failure:
                    agent.reports_received.append(report)
                    success = True
                    if event and not report.get("acted_on", False):
                        follow_up_action = agent.decide_action(event, is_follow_up=True)
                        agent.execute_action(event, follow_up_action)
                        report["acted_on"] = True
                        logging.info(
                            f"Step {self.schedule.steps}: {sender.role.value} {sender.unique_id} sent to "
                            f"{agent.role.value} {agent.unique_id}, action={follow_up_action.value}, "
                            f"event={event.get('type').value}"
                        )
        else:  # ReportingStructure.NONE
            neighbors = self.grid.get_neighbors(sender.pos, moore=True, include_center=False, radius=comm_radius)
            target_roles = []
            if self.org_structure == OrgStructure.FUNCTIONAL or regulatory_required:
                if sender.role == AgentRole.WORKER:
                    target_roles = [AgentRole.MANAGER]
                elif sender.role == AgentRole.MANAGER:
                    target_roles = [AgentRole.DIRECTOR]
                elif sender.role == AgentRole.DIRECTOR:
                    target_roles = [AgentRole.MANAGER]
            else:
                target_roles = [AgentRole.WORKER, AgentRole.MANAGER, AgentRole.DIRECTOR]
            for agent in self.schedule.agents:
                if agent != sender and agent.role in target_roles and agent in neighbors and random.random() > comm_failure:
                    agent.reports_received.append(report)
                    success = True
                    if event and not report.get("acted_on", False):
                        follow_up_action = agent.decide_action(event, is_follow_up=True)
                        agent.execute_action(event, follow_up_action)
                        report["acted_on"] = True
                        logging.info(
                            f"Step {self.schedule.steps}: {sender.role.value} {sender.unique_id} sent to "
                            f"{agent.role.value} {agent.unique_id}, action={follow_up_action.value}, "
                            f"event={event.get('type').value}"
                        )
        return success

    def log_metrics(self):
        comm_failure = self.get_current_comm_failure()
        schedule_adherence = (
            self.outcomes.tasks_completed_on_time / self.outcomes.total_tasks * 100
            if self.outcomes.total_tasks > 0 else 0
        )
        if self.schedule.steps > 1 and abs(schedule_adherence - self.previous_adherence) > 0.01:
            logging.info(
                f"Schedule Adherence changed from {self.previous_adherence:.2f}% to {schedule_adherence:.2f}% "
                f"at step {self.schedule.steps}"
            )
        self.previous_adherence = schedule_adherence
        metrics_data = {
            "Simulation_ID": self.simulation_id,
            "Step": self.schedule.steps,
            "Reporting_Structure": self.reporting_structure.value,
            "Org_Structure": self.org_structure.value,
            "Worker_SA": (
                np.mean([a.awareness.total_score() for a in self.schedule.agents if a.role == AgentRole.WORKER])
                if any(a.role == AgentRole.WORKER for a in self.schedule.agents) else 0
            ),
            "Manager_SA": (
                np.mean([a.awareness.total_score() for a in self.schedule.agents if a.role == AgentRole.MANAGER])
                if any(a.role == AgentRole.MANAGER for a in self.schedule.agents) else 0
            ),
            "Director_SA": (
                np.mean([a.awareness.total_score() for a in self.schedule.agents if a.role == AgentRole.DIRECTOR])
                if any(a.role == AgentRole.DIRECTOR for a in self.schedule.agents) else 0
            ),
            "Reporter_SA": (
                np.mean([a.awareness.total_score() for a in self.schedule.agents if a.role == AgentRole.REPORTER])
                if any(a.role == AgentRole.REPORTER for a in self.schedule.agents) else 0
            ),
            "Worker_Reports_Sent": (
                np.sum([a.reports_sent for a in self.schedule.agents if a.role == AgentRole.WORKER])
                if any(a.role == AgentRole.WORKER for a in self.schedule.agents) else 0
            ),
            "Manager_Reports_Sent": (
                np.sum([a.reports_sent for a in self.schedule.agents if a.role == AgentRole.MANAGER])
                if any(a.role == AgentRole.MANAGER for a in self.schedule.agents) else 0
            ),
            "Director_Reports_Sent": (
                np.sum([a.reports_sent for a in self.schedule.agents if a.role == AgentRole.DIRECTOR])
                if any(a.role == AgentRole.DIRECTOR for a in self.schedule.agents) else 0
            ),
            "Reporter_Reports_Sent": (
                np.sum([a.reports_sent for a in self.schedule.agents if a.role == AgentRole.REPORTER])
                if any(a.role == AgentRole.REPORTER for a in self.schedule.agents) else 0
            ),
            "Worker_Reports_Received": (
                np.sum([len(a.reports_received) for a in self.schedule.agents if a.role == AgentRole.WORKER])
                if any(a.role == AgentRole.WORKER for a in self.schedule.agents) else 0
            ),
            "Manager_Reports_Received": (
                np.sum([len(a.reports_received) for a in self.schedule.agents if a.role == AgentRole.MANAGER])
                if any(a.role == AgentRole.MANAGER for a in self.schedule.agents) else 0
            ),
            "Director_Reports_Received": (
                np.sum([len(a.reports_received) for a in self.schedule.agents if a.role == AgentRole.DIRECTOR])
                if any(a.role == AgentRole.DIRECTOR for a in self.schedule.agents) else 0
            ),
            "Reporter_Reports_Received": (
                np.sum([len(a.reports_received) for a in self.schedule.agents if a.role == AgentRole.REPORTER])
                if any(a.role == AgentRole.REPORTER for a in self.schedule.agents) else 0
            ),
            "Safety_Incidents": self.outcomes.safety_incidents,
            "Incident_Points": self.outcomes.incident_points,
            "Schedule_Adherence": schedule_adherence,
            "Cost_Overruns": self.outcomes.cost_overruns,
            "Comm_Failure_Rate": comm_failure,
            "Hazard_Events": self.event_counts[EventType.HAZARD],
            "Delay_Events": self.event_counts[EventType.DELAY],
            "Resource_Shortage_Events": self.event_counts[EventType.RESOURCE_SHORTAGE],
            "Total_Tasks": self.outcomes.total_tasks,
            "Tasks_Completed_On_Time": self.outcomes.tasks_completed_on_time,
            "Budget_Remaining": self.budget,
            "Equipment_Available": self.equipment_available,
            "Worker_Act_Count": (
                np.sum([a.actions_taken[ActionType.ACT] for a in self.schedule.agents if a.role == AgentRole.WORKER])
                if any(a.role == AgentRole.WORKER for a in self.schedule.agents) else 0
            ),
            "Manager_Act_Count": (
                np.sum([a.actions_taken[ActionType.ACT] for a in self.schedule.agents if a.role == AgentRole.MANAGER])
                if any(a.role == AgentRole.MANAGER for a in self.schedule.agents) else 0
            ),
            "Director_Act_Count": (
                np.sum([a.actions_taken[ActionType.ACT] for a in self.schedule.agents if a.role == AgentRole.DIRECTOR])
                if any(a.role == AgentRole.DIRECTOR for a in self.schedule.agents) else 0
            ),
            "Reporter_Act_Count": (
                np.sum([a.actions_taken[ActionType.ACT] for a in self.schedule.agents if a.role == AgentRole.REPORTER])
                if any(a.role == AgentRole.REPORTER for a in self.schedule.agents) else 0
            ),
            "Project_Phase": self.project_phase.value,
            "Critical_Tasks": len(self.critical_tasks),
            "Supplier_Communications": len(self.supplier_communication)
        }
        self.metrics_log.append(metrics_data)
        worker_act_count = metrics_data["Worker_Act_Count"]
        logging.debug(
            f"Metrics logged at step {self.schedule.steps}: "
            f"Schedule_Adherence={schedule_adherence:.2f}%, "
            f"Safety_Incidents={self.outcomes.safety_incidents}, "
            f"Worker_Act_Count={worker_act_count}, "
            f"Budget={self.budget:.2f}, "
            f"Equipment={self.equipment_available}"
        )
        print(
            f"Step {self.schedule.steps}: "
            f"Schedule Adherence={schedule_adherence:.2f}%, "
            f"Total Tasks={self.outcomes.total_tasks}, "
            f"Completed On Time={self.outcomes.tasks_completed_on_time}, "
            f"Safety Incidents={self.outcomes.safety_incidents}, "
            f"Worker Act={worker_act_count}, "
            f"Budget={self.budget:.2f}, "
            f"Equipment={self.equipment_available}, "
            f"Project Phase={self.project_phase.value}"
        )

    def log_agent_situational_awareness(self):
        try:
            sa_data = []
            if self.schedule.steps == 0:
                self.initial_sa_scores = {agent.unique_id: agent.awareness.total_score() for agent in self.schedule.agents}
            
            for agent in self.schedule.agents:
                sa_score = agent.awareness.total_score()
                sa_level = sa_score - self.initial_sa_scores.get(agent.unique_id, 0) if self.schedule.steps > 0 else 0
                sa_data.append({
                    "Simulation_ID": self.simulation_id,
                    "Step": self.schedule.steps,
                    "Agent_ID": agent.unique_id,
                    "Role": agent.role.value,
                    "SA_Score": sa_score,
                    "SA_Level": sa_level,
                    "Reports_Sent": agent.reports_sent,
                    "Reports_Received": len(agent.reports_received),
                    "Workload": agent.workload,
                    "Fatigue": agent.fatigue,
                    "Experience": agent.experience,
                    "Risk_Tolerance": agent.risk_tolerance
                })
            self.agent_sa_log.extend(sa_data)
            logging.debug(f"Logged situational awareness for {len(sa_data)} agents at step {self.schedule.steps}")
            print(f"Step {self.schedule.steps}: Logged situational awareness for {len(sa_data)} agents")
        except Exception as e:
            print(f"Error logging agent situational awareness at step {self.schedule.steps}: {e}")
            logging.error(f"SA logging error: {traceback.format_exc()}")

    def save_to_excel(self):
        max_retries = 3
        retry_delay = 5
        for attempt in range(max_retries):
            try:
                with FileLock(self.lock_filepath, timeout=30):
                    metrics_df = pd.DataFrame(self.metrics_log) if self.metrics_log else pd.DataFrame()
                    sa_df = pd.DataFrame(self.agent_sa_log) if self.agent_sa_log else pd.DataFrame()
                    model_data = pd.DataFrame()
                    agent_data = pd.DataFrame()
                    try:
                        model_data = self.datacollector.get_model_vars_dataframe()
                        agent_data = self.datacollector.get_agent_vars_dataframe()
                    except Exception as e:
                        print(f"Error collecting Mesa data at step {self.schedule.steps}: {e}")
                        logging.error(f"Mesa data collection error: {traceback.format_exc()}")

                    with pd.ExcelWriter(self.excel_filepath, engine='openpyxl', mode='w') as writer:
                        pd.DataFrame(self.configuration_log).to_excel(writer, sheet_name='Configuration', index=False)
                        if not metrics_df.empty:
                            metrics_df.to_excel(writer, sheet_name='Model_Metrics', index=False)
                        if not sa_df.empty:
                            sa_df.to_excel(writer, sheet_name='Agent_SA', index=False)
                        if not model_data.empty:
                            model_data.to_excel(writer, sheet_name='Mesa_Model_Data', index=False)
                        if not agent_data.empty:
                            agent_data.to_excel(writer, sheet_name='Mesa_Agent_Data', index=False)
                    logging.info(f"Data successfully written to {self.excel_filepath} at step {self.schedule.steps}, attempt {attempt + 1}")
                    print(f"Data successfully written to {self.excel_filepath} at step {self.schedule.steps}, attempt {attempt + 1}")
                    self.metrics_log = []
                    self.agent_sa_log = []
                    return
            except Timeout as e:
                print(f"Timeout saving to Excel at step {self.schedule.steps}, attempt {attempt + 1}: {e}")
                logging.error(f"Excel save timeout at attempt {attempt + 1}: {traceback.format_exc()}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                continue
            except Exception as e:
                print(f"Error saving to Excel at step {self.schedule.steps}, attempt {attempt + 1}: {e}")
                logging.error(f"Excel save error at attempt {attempt + 1}: {traceback.format_exc()}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                continue
        try:
            metrics_df = pd.DataFrame(self.metrics_log) if self.metrics_log else pd.DataFrame()
            sa_df = pd.DataFrame(self.agent_sa_log) if self.agent_sa_log else pd.DataFrame()
            model_data = pd.DataFrame()
            agent_data = pd.DataFrame()
            try:
                model_data = self.datacollector.get_model_vars_dataframe()
                agent_data = self.datacollector.get_agent_vars_dataframe()
            except Exception as e:
                print(f"Error collecting Mesa data for CSV fallback: {e}")
                logging.error(f"Mesa data collection error for CSV: {traceback.format_exc()}")

            if not metrics_df.empty:
                metrics_df.to_csv(
                    self.csv_filepath.replace('.csv', '_metrics.csv'),
                    mode='a',
                    header=not os.path.exists(self.csv_filepath.replace('.csv', '_metrics.csv')),
                    index=False
                )
            if not sa_df.empty:
                sa_df.to_csv(
                    self.csv_filepath.replace('.csv', '_agent_sa.csv'),
                    mode='a',
                    header=not os.path.exists(self.csv_filepath.replace('.csv', '_agent_sa.csv')),
                    index=False
                )
            if not model_data.empty:
                model_data.to_csv(
                    self.csv_filepath.replace('.csv', '_model_data.csv'),
                    mode='a',
                    header=not os.path.exists(self.csv_filepath.replace('.csv', '_model_data.csv')),
                    index=False
                )
            if not agent_data.empty:
                agent_data.to_csv(
                    self.csv_filepath.replace('.csv', '_agent_data.csv'),
                    mode='a',
                    header=not os.path.exists(self.csv_filepath.replace('.csv', '_agent_data.csv')),
                    index=False
                )
            logging.info(f"Data saved to CSV files at {self.csv_filepath.replace('.csv', '_*.csv')} as fallback")
            print(f"Data saved to CSV files at {self.csv_filepath.replace('.csv', '_*.csv')} as fallback")
        except Exception as e:
            print(f"Error saving to CSV at step {self.schedule.steps}: {e}")
            logging.error(f"CSV save error: {traceback.format_exc()}")

    def step(self):
        try:
            logging.info(f"Executing step {self.schedule.steps + 1}, Budget={self.budget:.2f}, Equipment={self.equipment_available}")
            print(f"Executing step {self.schedule.steps + 1}")
            self.update_project_phase()  # Update phase at each step
            if self.schedule.steps % 5 == 0:
                if self.budget < 900000:
                    self.budget += 200000
                    logging.info(f"Replenished budget at step {self.schedule.steps}, new total={self.budget:.2f}")
                    print(f"Step {self.schedule.steps}: Replenished budget, new total={self.budget:.2f}")
                if self.equipment_available < 400:
                    self.equipment_available += 100
                    logging.info(f"Replenished equipment at step {self.schedule.steps}, new total={self.equipment_available}")
                    print(f"Step {self.schedule.steps}: Replenished equipment, new total={self.equipment_available}")
            self.schedule.step()
            self.datacollector.collect(self)
            self.log_metrics()
            if self.schedule.steps % 10 == 0:
                self.log_agent_situational_awareness()
            logging.info(f"Completed step {self.schedule.steps}, Budget={self.budget:.2f}, Equipment={self.equipment_available}")
            print(f"Completed step {self.schedule.steps}")
        except Exception as e:
            print(f"Error in model step {self.schedule.steps + 1}: {e}")
            logging.error(f"Step error: {traceback.format_exc()}")

    def run_simulation(self, steps: int = 100):
        logging.info(f"Starting simulation with {steps} steps, simulation_id={self.simulation_id}")
        print(f"Starting simulation with {steps} steps...")
        print(f"Simulation ID: {self.simulation_id}")
        print(f"Reporting structure: {self.reporting_structure.value}, Org structure: {self.org_structure.value}")
        print(f"Excel output: {self.excel_filepath}")
        print(
            f"Agent counts: "
            f"Workers={len([a for a in self.schedule.agents if a.role == AgentRole.WORKER])}, "
            f"Managers={len([a for a in self.schedule.agents if a.role == AgentRole.MANAGER])}, "
            f"Directors={len([a for a in self.schedule.agents if a.role == AgentRole.DIRECTOR])}, "
            f"Reporters={len([a for a in self.schedule.agents if a.role == AgentRole.REPORTER])}"
        )
        for _ in range(steps):
            self.step()
        self.save_to_excel()
        logging.info(f"Simulation completed: {self.simulation_id}")
        print(f"Simulation completed: {self.simulation_id}")