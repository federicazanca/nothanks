from game_state import GameState

class Player:
    """Player class to define player's properties."""
    def __init__(self, chips) -> None:
        self.chips = chips
        self.cards = []

    def play(self, game_state: GameState) -> bool:
        """Returns True if player takes, False otherwise."""
        pass
