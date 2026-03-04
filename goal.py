# core/goal.py

class Goal:
    def __init__(self, outcome: str, constraints=None, success_conditions=None):
        self.outcome = outcome
        self.constraints = constraints or []
        self.success_conditions = success_conditions or []

        self.iterations = 0
        self.max_iterations = 3
        self.progress = 0.0

    def invariant_valid(self):
        """
        Controls the agent loop.
        Stops when iteration limit reached.
        """
        return self.iterations < self.max_iterations