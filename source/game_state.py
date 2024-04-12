from player import Player
import random

class GameState:
    """Represents a game and simulates it."""
    def __init__(self) -> None:
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
