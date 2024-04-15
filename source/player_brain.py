import numpy as np
from sklearn.linear_model import LinearRegression

class PlayerBrain:
    """Base class for simulating the player decisions."""

    def decide(self, state: np.ndarray) -> float:
        """Returns a float between 0.0 and 1.0."""
        raise NotImplementedError("Method should be overridden in child class")
    
    def train(self, state: np.ndarray, expected: float, intensity: float) -> None:
        """Trains the brain towards `expected` when deciding on `state`, with learning rate amplified by `intensity`."""
        raise NotImplementedError("Method should be overridden in child class")

class DummyPlayerBrain(PlayerBrain):
    """Dummy which always decides 0."""

    def decide(self, state: np.ndarray) -> float:
        return 0.0
    
    def train(self, state: np.ndarray, expected: float, intensity: float) -> None:
        pass

class LinearRegressionBrain(PlayerBrain):
    def __init__(self) -> None:
        self.model = LinearRegression()
        self.model.fit([[0.0]*34*6], [0.0])

    def decide(self, state: np.ndarray) -> float:
        input = []
        for column in state:
            input.extend(column)
        return self.model.predict([input])
    
    def train(self, state: np.ndarray, expected: float, intensity: float) -> None:
        pass
