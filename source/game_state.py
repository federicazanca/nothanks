import random
import numpy as np

class GameState:
    """Represents a game and simulates it."""

    def __init__(self) -> None:
        from player import Player
        self.players = [Player(11) for _ in range(5)]
        self.pool = 0
        self.deck = self._generate_deck()
        self.card = self.deck.pop()
        self.active_player_index = 0
    
    def play(self) -> bool:
        """Simulates an action in the game. Returns True if game is finished."""
        player = self.players[self.active_player_index]
        if player.play(self):
            player.cards.append(self.card)
            player.chips += self.pool
            self.pool = 0
            if len(self.deck) == 0:
                self.card = 0
                return True
            self.card = self.deck.pop()
        else:
            player.chips -= 1
            self.pool += 1
            self.active_player_index += 1
            self.active_player_index %= 5
        return False

    @staticmethod
    def _generate_deck() -> list[int]:
        """Shuffles a deck of values 3 to 35, removing 9 cards."""
        deck = [i for i in range(3, 36)]
        random.shuffle(deck)
        return deck[:-9]
    
    def into_ml_matrix(self):
        """Return the ML representation."""
        deck_col = [float(self.pool)]
        for i in range(3,36):
            if self.card == i:
                deck_col.append(1.0)
            else:
                deck_col.append(0.0)
        matrix = np.array([deck_col])
        for player in self.players:
            matrix = np.append(matrix, [player.into_ml_column()], axis=0)
        return matrix
