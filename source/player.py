from game_state import GameState
from player_brain import PlayerBrain
from enum import Enum
import numpy as np

class PlayerAction(Enum):
    PASS = 0
    TAKE = 1

class Player:
    """Player class to define player's properties."""

    def __init__(self, brain: PlayerBrain, chips: int) -> None:
        self.brain = brain
        self.chips = chips
        self.cards = []

    def play(self, game_state: GameState) -> PlayerAction:
        """Returns the action decided."""
        if self.brain.decide(game_state.into_ml_matrix()) >= 0.5:
            return PlayerAction.TAKE
        else:
            return PlayerAction.PASS

    def into_ml_column(self) -> np.ndarray[float]:
        """Returns the ML column representation."""
        player_col = [float(self.chips)]
        for i in range(3,36):
            if i in self.cards:
                player_col.append(1.0)
            else:
                player_col.append(0.0)
        return np.array(player_col)
    
    def score(self) -> int:
        """Returns the score of the player."""
        score = 0
        cards = self.cards.copy()
        cards.sort(reverse=True)
        card = 0
        while True:
            if len(cards) == 0:
                break
            next_card = cards.pop()
            if not next_card + 1 == card:
                score += card
            card = next_card
        return score - self.chips
