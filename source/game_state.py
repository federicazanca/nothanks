from player_brain import PlayerBrain
from enum import Enum
import random
import numpy as np

class GameAction(Enum):
    PASS = 0
    TAKE = 1
    FORCED = 2

class GameState:
    """Represents a game and simulates it."""

    def __init__(self, brains: list[PlayerBrain], deck: list[int] = None) -> None:
        """Creates a new game for the given Brains, using the given deck or shuffling a new one otherwise."""
        from player import Player
        if deck == None:
            deck = self._generate_deck()
        self.players: list[Player] = [Player(brain, 11) for brain in brains]
        self.pool: int = 0
        self.deck: list[int] = deck
        self.card: int | None = self.deck.pop()
        self.active_player_index: int = 0
    
    def play(self) -> GameAction | None:
        """Simulates an action in the game, reporting the current player's action, or None if the game is over."""
        from player import PlayerAction
        if self.card == None:
            return None
        player = self.players[self.active_player_index]
        must_take = player.chips == 0
        if must_take or player.play(self) == PlayerAction.TAKE:
            player.cards.append(self.card)
            player.chips += self.pool
            self.pool = 0
            if len(self.deck) == 0:
                self.card = None
            else:
                self.card = self.deck.pop()
            if must_take:
                return GameAction.FORCED
            else:
                return GameAction.TAKE
        else:
            player.chips -= 1
            self.pool += 1
            self.active_player_index += 1
            self.active_player_index %= 5
            return GameAction.PASS

    @staticmethod
    def _generate_deck() -> list[int]:
        """Shuffles a deck of values 3 to 35, removing 9 cards."""
        deck = [i for i in range(3, 36)]
        random.shuffle(deck)
        return deck[:-9]
    
    def into_ml_matrix(self) -> np.ndarray:
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
