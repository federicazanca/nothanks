from game_state import GameState
import numpy as np

class Player:
    """Player class to define player's properties."""
    def __init__(self, chips: int) -> None:
        self.chips = chips
        self.cards = []

    def play(self, game_state: GameState) -> bool:
        """Returns True if player takes, False otherwise."""
        return self.chips == 0

    def into_ml_column(self) -> list[float]:
        """Returns the ML column representation."""
        player_col = [float(self.chips)]
        for i in range(3,36):
            for n in self.cards:
                if self.cards(n) == i:
                    player_col.append(1.0)
                else:
                    player_col.append(0.0)
        return player_col
