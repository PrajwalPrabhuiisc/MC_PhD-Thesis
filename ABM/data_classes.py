from dataclasses import dataclass

@dataclass
class SituationalAwareness:
    perception: float = 0.0
    comprehension: float = 0.0
    projection: float = 0.0

    def total_score(self) -> float:
        return (self.perception + self.comprehension + self.projection) / 3

@dataclass
class ProjectOutcomes:
    def __init__(self):
        self.safety_incidents = 0
        self.incident_points = 0.0
        self.total_tasks = 0
        self.tasks_completed_on_time = 0
        self.cost_overruns = 0.0
        self.total_tasks_added_this_step = False  # New flag