from game_state import GameState
from player_brain import DummyPlayerBrain

if __name__ == "__main__":
    game = GameState([DummyPlayerBrain() for _ in range(5)])
    while True:
        if game.play():
            break
    print(game.into_ml_matrix())
