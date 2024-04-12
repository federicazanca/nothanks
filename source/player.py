from game_state import GameState

class Player:
    """Player class to define player's properties."""
    def __init__(self, chips: int) -> None:
        self.chips = chips
        self.cards = []

    def play(self, game_state: GameState) -> bool:
        """Returns True if player takes, False otherwise."""
        return self.chips == 0

    def into_ml_column(self) -> np.ndarray[float]:
        """Returns the ML column representation."""
        player_col = [float(self.chips)]
        for i in range(3,36):
            for n in self.cards:
                if self.cards(n) == i:
                    player_col.append(1.0)
                else:
                    player_col.append(0.0)
        return np.array(player_col)
    
    def score(self) -> int:
        """Returns the score of the player."""
        score = 0
        self.cards.sort(reverse=True)
        card = 0
        while True:
            if len(self.cards) == 0:
                break
            next_card = self.cards.pop()
            if not next_card + 1 == card:
                score += card
            card = next_card
        return score - self.chips
