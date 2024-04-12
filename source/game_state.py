from player import Player
import random

class GameState:
    def __init__(self) -> None:
        self.players = [Player(11), 5]
        self.pool = 0
        self.deck = self._generate_deck()
        self.card = self.deck.pop()
        self.active_player_index = 0

    @staticmethod
    def _generate_deck():
        deck = [i for i in range(3, 36)]
        random.shuffle(deck)
        return deck[:-9]
