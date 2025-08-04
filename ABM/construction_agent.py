import random
import logging
from typing import Dict, List, Optional

import numpy as np
from enums import AgentRole, EventType, ActionType, OrgStructure, ReportingStructure, ProjectPhase, Criticality
from data_classes import SituationalAwareness
from construction_model import ConstructionModel
from decision_model import DecisionModel

logging.basicConfig(filename='simulation_agent.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionAgent:
    def __init__(self, unique_id: int, model: ConstructionModel, role: AgentRole, pos: tuple):
        self.unique_id = unique_id
        self.model = model
        self.role = role
        self.pos = pos
        self.awareness = SituationalAwareness()
        self.reports_sent = 0
        self.reports_received: List[Dict] = []
        self.actions_taken = {action: 0 for action in ActionType}
        self.workload = random.uniform(0, 5)
        self.fatigue = random.uniform(0, 1)
        self.experience = random.uniform(0, 1)
        self.risk_tolerance = random.uniform(0, 1)
        self.detection_accuracy = {
            AgentRole.WORKER: model.worker_detection,
            AgentRole.MANAGER: model.manager_detection,
            AgentRole.REPORTER: model.reporter_detection,
            AgentRole.DIRECTOR: model.director_detection
        }[role]
        self.reporting_probability = {
            AgentRole.WORKER: model.worker_reporting,
            AgentRole.MANAGER: model.manager_reporting,
            AgentRole.REPORTER: model.reporter_reporting,
            AgentRole.DIRECTOR: model.director_reporting
        }[role]
        self.detection_modifier = 1.5 if role == AgentRole.REPORTER else 1.0
        self.decision_model = DecisionModel()

    def step(self):
        for event in self.model.get_events():
            self.observe_event(event)

        for report in self.reports_received[:]:
            event_data = report.get("event")
            if event_data and not report.get("acted_on", False):
                action = self.decide_action(event_data, is_follow_up=True)
                self.execute_action(event_data, action)
                report["acted_on"] = True
                logging.info(
                    f"Agent {self.unique_id} ({self.role.value}) acted on report with severity {event_data.get('severity', 0):.2f}, "
                    f"action={action.value}, at step {self.model.schedule.steps}"
                )
                self.reports_received.remove(report)

    def observe_event(self, event: Optional[Dict]) -> bool:
        if event is None:
            return False

        org_sa_modifier = 1.2 if self.model.org_structure == OrgStructure.FLAT else 1.0 if self.model.org_structure == OrgStructure.FUNCTIONAL else 0.8
        sa_reduction = 0.7 if self.model.outcomes.safety_incidents > 5 else 1.0
        phase_modifier = 1.5 if self.model.project_phase == ProjectPhase.FOUNDATION else 1.0

        if random.random() < self.detection_accuracy * self.detection_modifier:
            severity = event.get("severity", 0.5)
            noise_std = 0.2 + 0.3 * self.fatigue
            random_noise = random.gauss(0, noise_std)
            
            if self.role == AgentRole.REPORTER:
                self.awareness.perception = min(
                    self.awareness.perception + self.detection_accuracy * 50 * (1 + random_noise) * severity * (1 - self.fatigue) * org_sa_modifier * sa_reduction * phase_modifier, 100)
                self.awareness.comprehension = min(
                    self.awareness.comprehension + self.detection_accuracy * 30 * (1 + random_noise) * severity * (1 - self.workload / 5) * org_sa_modifier * sa_reduction * phase_modifier, 100)
                self.awareness.projection = min(
                    self.awareness.projection + self.detection_accuracy * 20 * (1 + random_noise) * severity * self.experience * org_sa_modifier * sa_reduction * phase_modifier, 100)
            else:
                self.awareness.perception = min(
                    self.awareness.perception + self.detection_accuracy * 40 * (1 + random_noise) * severity * (1 + self.experience) * org_sa_modifier * sa_reduction * phase_modifier, 100)
                self.awareness.comprehension = min(
                    self.awareness.comprehension + self.detection_accuracy * 20 * (1 + random_noise) * severity * (1 - self.workload / 5) * org_sa_modifier * sa_reduction * phase_modifier, 100)
                self.awareness.projection = min(
                    self.awareness.projection + self.detection_accuracy * 15 * (1 + random_noise) * severity * self.experience * org_sa_modifier * sa_reduction * phase_modifier, 100)

            logging.debug(
                f"Agent {self.unique_id} ({self.role.value}) observed event {event.get('type', 'None').value} "
                f"at step {self.model.schedule.steps}, SA updated: "
                f"P={self.awareness.perception:.2f}, C={self.awareness.comprehension:.2f}, Proj={self.awareness.projection:.2f}, "
                f"Random_Noise={random_noise:.2f}"
            )

            action = self.decide_action(event)
            regulatory_required = event["type"] == EventType.HAZARD and event["severity"] >= 0.5
            if action == ActionType.ACT and (event["type"] != EventType.HAZARD or (event["type"] == EventType.HAZARD and self.role == AgentRole.WORKER and not self.model.hazard_acted_this_step)):
                self.execute_action(event, action)
                if event["type"] == EventType.HAZARD:
                    self.model.hazard_acted_this_step = True
                logging.info(
                    f"Agent {self.unique_id} ({self.role.value}) acted on {event.get('type').value} event, "
                    f"at step {self.model.schedule.steps}"
                )
            elif regulatory_required or random.random() < self.reporting_probability or event["criticality"] == Criticality.CRITICAL:
                report = {"event": event, "source": self.role.value, "timestamp": self.model.schedule.steps}
                if self.send_report(report):
                    self.reports_sent += 1
                    logging.debug(
                        f"Agent {self.unique_id} ({self.role.value}) sent report for event {event.get('type').value} "
                        f"at step {self.model.schedule.steps}"
                    )
            return True
        return False

    def send_report(self, report: Dict) -> bool:
        return self.model.send_report(self, report)

    def decide_action(self, event: Dict, is_follow_up: bool = False) -> ActionType:
        severity = event.get("severity", 0.5)
        criticality = event.get("criticality", Criticality.NON_CRITICAL)
        phase = self.model.project_phase
        recent_hazards = len([e for e in self.model.organizational_memory[EventType.HAZARD] if e["timestamp"] >= self.model.schedule.steps - 5])
        resource_availability = self.model.equipment_available / 500
        time_pressure = 1.0 if self.model.schedule.steps > 80 else 0.5  # High pressure near end of 100 steps
        stress = min(self.workload / 5 + self.fatigue, 1.0)

        # Safety-first decision logic for hazards
        if event["type"] == EventType.HAZARD:
            if severity > 0.8:
                return ActionType.ESCALATE  # Immediate escalation for high-severity hazards
            elif severity >= 0.5:
                return ActionType.ACT if self.model.budget >= 1000 else ActionType.ESCALATE
            else:
                return ActionType.REPORT  # Monitor low-severity hazards

        # Critical path delays
        if event["type"] == EventType.DELAY and criticality == Criticality.CRITICAL:
            return ActionType.ACT

        # Resource shortage logic
        if event["type"] == EventType.RESOURCE_SHORTAGE:
            if severity < 0.4 and resource_availability > 0.5:
                return ActionType.SUBSTITUTE  # Try substitution for low-severity shortages
            else:
                self.model.supplier_communication.append({"step": self.model.schedule.steps, "event": event})
                return ActionType.ESCALATE

        # Decision model inputs
        inputs = np.array([[
            self.workload,
            self.fatigue,
            severity,
            self.experience,
            time_pressure,
            resource_availability,
            self.risk_tolerance,
            stress,
            1.0 if recent_hazards > 0 else 0.0,
            1.0 if phase == ProjectPhase.FOUNDATION else 0.5 if phase == ProjectPhase.FRAMING else 0.0,
            1.0 if criticality == Criticality.CRITICAL else 0.0
        ]])
        probs = self.decision_model.predict_proba(inputs)[0]
        actions = [ActionType.REPORT, ActionType.ACT, ActionType.ESCALATE, ActionType.SUBSTITUTE]
        action = np.random.choice(actions, p=probs)
        logging.debug(
            f"Agent {self.unique_id} ({self.role.value}) decided action {action.value} for event {event.get('type').value} "
            f"at step {self.model.schedule.steps}, probs={probs}"
        )
        return action

    def execute_action(self, event: Dict, action: ActionType) -> bool:
        success = False
        severity = event.get("severity", 0.5)
        noise_std = 0.2 + 0.3 * self.fatigue
        random_noise = random.gauss(0, noise_std)
        org_sa_modifier = 1.2 if self.model.org_structure == OrgStructure.FLAT else 1.0 if self.model.org_structure == OrgStructure.FUNCTIONAL else 0.8
        sa_reduction = 0.7 if self.model.outcomes.safety_incidents > 5 else 1.0
        phase_modifier = 1.5 if self.model.project_phase == ProjectPhase.FOUNDATION else 1.0

        # Priority-based budget allocation
        is_critical = event.get("criticality", Criticality.NON_CRITICAL) == Criticality.CRITICAL
        is_high_severity_hazard = event["type"] == EventType.HAZARD and severity > 0.8
        budget_required = {
            ActionType.REPORT: 1000,
            ActionType.ACT: 1000 if event["type"] != EventType.HAZARD else 10000,
            ActionType.ESCALATE: 1500,
            ActionType.SUBSTITUTE: 500
        }[action]
        budget_check = self.model.budget >= budget_required
        if is_high_severity_hazard or is_critical:
            budget_check = True  # Override budget for critical or high-severity hazards

        if action == ActionType.REPORT:
            report = {"event": event, "source": self.role.value, "timestamp": self.model.schedule.steps}
            if self.send_report(report):
                self.reports_sent += 1
                self.actions_taken[action] += 1
                if not is_high_severity_hazard:
                    self.model.budget -= budget_required
                success = True
                logging.debug(
                    f"Agent {self.unique_id} ({self.role.value}) executed REPORT action for event {event.get('type').value} "
                    f"at step {self.model.schedule.steps}, budget={self.model.budget:.2f}"
                )
        elif action == ActionType.ACT:
            if not budget_check:
                logging.warning(
                    f"Agent {self.unique_id} ({self.role.value}) failed to ACT on {event.get('type').value} "
                    f"due to insufficient budget {self.model.budget:.2f} at step {self.model.schedule.steps}"
                )
                return False
            self.awareness.perception = min(
                self.awareness.perception + self.detection_accuracy * 20 * (1 + random_noise) * severity * (1 + self.experience) * org_sa_modifier * sa_reduction * phase_modifier, 100)
            self.awareness.comprehension = min(
                self.awareness.comprehension + self.detection_accuracy * 15 * (1 + random_noise) * severity * (1 - self.workload / 5) * org_sa_modifier * sa_reduction * phase_modifier, 100)
            self.awareness.projection = min(
                self.awareness.projection + self.detection_accuracy * 10 * (1 + random_noise) * severity * self.experience * org_sa_modifier * sa_reduction * phase_modifier, 100)
            if event["type"] == EventType.HAZARD:
                self.model.outcomes.safety_incidents += 1
                self.model.outcomes.incident_points += severity * 100
                if not is_high_severity_hazard:
                    self.model.budget -= budget_required
                if self.model.equipment_available > 0:
                    self.model.equipment_available -= 1
                logging.info(
                    f"Agent {self.unique_id} ({self.role.value}) triggered safety incident for HAZARD, "
                    f"severity={severity:.2f}, incident_points={self.model.outcomes.incident_points:.1f}, "
                    f"budget={self.model.budget:.2f}, equipment={self.model.equipment_available} "
                    f"at step {self.model.schedule.steps}"
                )
            elif event["type"] == EventType.DELAY:
                self.model.outcomes.tasks_completed_on_time += 1
                if not is_critical:
                    self.model.budget -= budget_required
                if self.role == AgentRole.MANAGER and self.experience > 0.7 and random.random() < 0.8:
                    if budget_check:
                        self.model.outcomes.tasks_completed_on_time += 2
                        if not is_critical:
                            self.model.budget -= budget_required
                        logging.info(
                            f"Agent {self.unique_id} (Manager) completed extra tasks for DELAY, "
                            f"budget={self.model.budget:.2f} at step {self.model.schedule.steps}"
                        )
                logging.info(
                    f"Agent {self.unique_id} ({self.role.value}) completed task for DELAY, "
                    f"budget={self.model.budget:.2f} at step {self.model.schedule.steps}"
                )
            elif event["type"] == EventType.RESOURCE_SHORTAGE:
                if self.model.equipment_available > 0:
                    if not is_critical:
                        self.model.budget -= 3000
                    self.model.equipment_available -= 1
                    logging.info(
                        f"Agent {self.unique_id} ({self.role.value}) used equipment for RESOURCE_SHORTAGE, "
                        f"budget={self.model.budget:.2f}, equipment={self.model.equipment_available} "
                        f"at step {self.model.schedule.steps}"
                    )
            self.actions_taken[action] += 1
            success = True
            logging.debug(
                f"Agent {self.unique_id} ({self.role.value}) updated SA for ACT on {event.get('type').value}: "
                f"P={self.awareness.perception:.2f}, C={self.awareness.comprehension:.2f}, Proj={self.awareness.projection:.2f}, "
                f"Random_Noise={random_noise:.2f}"
            )
        elif action == ActionType.ESCALATE:
            if not budget_check:
                logging.warning(
                    f"Agent {self.unique_id} ({self.role.value}) failed to ESCALATE on {event.get('type').value} "
                    f"due to insufficient budget {self.model.budget:.2f} at step {self.model.schedule.steps}"
                )
                return False
            self.awareness.perception = min(
                self.awareness.perception + self.detection_accuracy * 15 * (1 + random_noise) * severity * (1 + self.experience) * org_sa_modifier * sa_reduction * phase_modifier, 100)
            self.awareness.comprehension = min(
                self.awareness.comprehension + self.detection_accuracy * 10 * (1 + random_noise) * severity * (1 - self.workload / 5) * org_sa_modifier * sa_reduction * phase_modifier, 100)
            self.awareness.projection = min(
                self.awareness.projection + self.detection_accuracy * 8 * (1 + random_noise) * severity * self.experience * org_sa_modifier * sa_reduction * phase_modifier, 100)
            report = {"event": event, "source": self.role.value, "timestamp": self.model.schedule.steps}
            if self.send_report(report):
                self.reports_sent += 1
                self.actions_taken[action] += 1
                if not is_high_severity_hazard:
                    self.model.budget -= budget_required
                success = True
                logging.debug(
                    f"Agent {self.unique_id} ({self.role.value}) executed ESCALATE action for event {event.get('type').value} "
                    f"at step {self.model.schedule.steps}, budget={self.model.budget:.2f}, "
                    f"SA updated: P={self.awareness.perception:.2f}, C={self.awareness.comprehension:.2f}, Proj={self.awareness.projection:.2f}, "
                    f"Random_Noise={random_noise:.2f}"
                )
        elif action == ActionType.SUBSTITUTE:
            if not budget_check:
                logging.warning(
                    f"Agent {self.unique_id} ({self.role.value}) failed to SUBSTITUTE on {event.get('type').value} "
                    f"due to insufficient budget {self.model.budget:.2f} at step {self.model.schedule.steps}"
                )
                return False
            self.model.budget -= budget_required
            self.actions_taken[action] += 1
            success = True
            logging.info(
                f"Agent {self.unique_id} ({self.role.value}) executed SUBSTITUTE action for event {event.get('type').value} "
                f"at step {self.model.schedule.steps}, budget={self.model.budget:.2f}"
            )
        return success