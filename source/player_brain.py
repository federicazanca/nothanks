import numpy as np

class PlayerBrain:
    """Base class for simulating the player decisions."""

    def decide(self, state: np.ndarray) -> float:
        """Returns a float between 0.0 and 1.0."""
        raise NotImplementedError("Method should be overridden in child class")

class DummyPlayerBrain(PlayerBrain):
    """Dummy which always decides 0."""

    def decide(self, state: np.ndarray) -> float:
        return 0.0
