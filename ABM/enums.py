from enum import Enum

class ReportingStructure(Enum):
    DEDICATED = "dedicated"
    SELF = "self"
    NONE = "none"

class OrgStructure(Enum):
    FUNCTIONAL = "functional"
    FLAT = "flat"
    HIERARCHICAL = "hierarchical"

class AgentRole(Enum):
    WORKER = "worker"
    MANAGER = "manager"
    DIRECTOR = "director"
    REPORTER = "reporter"

class EventType(Enum):
    HAZARD = "hazard"
    DELAY = "delay"
    RESOURCE_SHORTAGE = "resource_shortage"

class ActionType(Enum):
    REPORT = "report"
    ACT = "act"
    ESCALATE = "escalate"
    SUBSTITUTE = "substitute"  # New action for resource substitution

class ProjectPhase(Enum):
    FOUNDATION = "foundation"
    FRAMING = "framing"
    INTERIOR = "interior"

class Criticality(Enum):
    CRITICAL = "critical"
    NON_CRITICAL = "non_critical"
