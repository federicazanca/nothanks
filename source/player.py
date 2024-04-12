"""Player class to define player's properties."""
from game_state import GameState

class Player:
    def __init__(self, chips):
        self.chips = chips
        self.cards = []
        pass

    def play(self, game_state:GameState):
        pass

