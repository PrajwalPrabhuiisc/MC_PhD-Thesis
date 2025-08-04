from sklearn.linear_model import LogisticRegression
import numpy as np

class DecisionModel:
    def __init__(self):
        self.model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
        self._train_model()

    def _train_model(self):
        # Training data: [workload, fatigue, event_severity, experience, time_pressure, resource_availability, risk_tolerance, stress, recent_hazard, project_phase, criticality]
        X = np.array([
            [1, 0.2, 1.0, 0.5, 0.2, 0.8, 0.5, 0.5, 0.0, 1.0, 1.0],  # HAZARD, foundation, critical
            [3, 0.7, 1.0, 0.3, 0.6, 0.5, 0.7, 1.0, 1.0, 1.0, 1.0],  # HAZARD, high workload
            [2, 0.5, 0.7, 0.6, 0.4, 0.7, 0.4, 0.5, 0.0, 0.5, 1.0],  # DELAY, framing, critical
            [4, 0.8, 0.7, 0.2, 0.8, 0.3, 0.6, 1.0, 0.0, 0.5, 0.0],  # DELAY, framing, non-critical
            [2, 0.3, 0.5, 0.7, 0.4, 0.9, 0.3, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE, interior
            [5, 0.9, 0.5, 0.1, 1.0, 0.2, 0.8, 1.0, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE, high stress
            [1, 0.1, 1.0, 0.9, 0.2, 0.9, 0.2, 0.5, 1.0, 1.0, 1.0],  # HAZARD, experienced
            [3, 0.6, 0.7, 0.4, 0.6, 0.6, 0.5, 0.5, 0.0, 0.5, 1.0],  # DELAY, balanced
            [2, 0.4, 0.5, 0.8, 0.4, 0.8, 0.4, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE
            [4, 0.7, 1.0, 0.3, 0.8, 0.4, 0.6, 1.0, 1.0, 1.0, 1.0],  # HAZARD, high risk
            [2, 0.5, 1.0, 0.6, 0.5, 0.7, 0.5, 0.5, 1.0, 1.0, 1.0],  # HAZARD
            [3, 0.6, 0.7, 0.5, 0.6, 0.6, 0.4, 0.5, 0.0, 0.5, 1.0],  # DELAY
            [1, 0.3, 0.5, 0.7, 0.3, 0.9, 0.3, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE
            [5, 0.8, 1.0, 0.2, 0.9, 0.3, 0.7, 1.0, 1.0, 1.0, 1.0],  # HAZARD
            [2, 0.4, 0.7, 0.6, 0.4, 0.8, 0.4, 0.5, 0.0, 0.5, 0.0],  # DELAY
            [3, 0.5, 0.5, 0.5, 0.5, 0.7, 0.5, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE
            [1, 0.2, 1.0, 0.8, 0.2, 0.9, 0.3, 0.5, 1.0, 1.0, 1.0],  # HAZARD
            [4, 0.7, 0.7, 0.3, 0.7, 0.4, 0.6, 1.0, 0.0, 0.5, 0.0],  # DELAY
            [2, 0.3, 0.5, 0.7, 0.3, 0.8, 0.4, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE
            [3, 0.6, 1.0, 0.4, 0.6, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0],  # HAZARD
            [2, 0.4, 0.7, 0.6, 0.4, 0.7, 0.4, 0.5, 0.0, 0.5, 0.0],  # DELAY
            [1, 0.2, 0.5, 0.8, 0.2, 0.9, 0.3, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE
            [5, 0.9, 1.0, 0.1, 0.9, 0.2, 0.8, 1.0, 1.0, 1.0, 1.0],  # HAZARD
            [3, 0.5, 0.7, 0.5, 0.5, 0.6, 0.5, 0.5, 0.0, 0.5, 0.0],  # DELAY
            [2, 0.3, 0.5, 0.7, 0.3, 0.8, 0.4, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE
            [4, 0.7, 1.0, 0.3, 0.7, 0.4, 0.6, 1.0, 1.0, 1.0, 1.0],  # HAZARD
            [2, 0.4, 0.7, 0.6, 0.4, 0.7, 0.4, 0.5, 0.0, 0.5, 0.0],  # DELAY
            [1, 0.2, 0.5, 0.8, 0.2, 0.9, 0.3, 0.5, 0.0, 0.0, 0.0],  # RESOURCE_SHORTAGE
            [3, 0.6, 1.0, 0.4, 0.6, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0],  # HAZARD
            [2, 0.4, 0.7, 0.6, 0.4, 0.7, 0.4, 0.5, 0.0, 0.5, 0.0]   # DELAY
        ])
        y = np.array([
            'escalate', 'act', 'act', 'report', 'substitute', 'escalate', 'act', 'report', 'substitute', 'escalate',
            'escalate', 'act', 'substitute', 'escalate', 'act', 'substitute', 'act', 'report', 'substitute', 'escalate',
            'act', 'substitute', 'escalate', 'act', 'substitute', 'escalate', 'act', 'substitute', 'escalate', 'act'
        ])
        self.model.fit(X, y)

    def predict_proba(self, inputs):
        return self.model.predict_proba(inputs)
    