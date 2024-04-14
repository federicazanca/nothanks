from game_state import GameState
from player_brain import DummyPlayerBrain

if __name__ == "__main__":
    game = GameState([DummyPlayerBrain() for _ in range(5)])
    while True:
        if game.play() == None:
            break
    for player in game.players:
        print(f"{player.chips} -> {player.cards}")
    print(game.into_ml_matrix())
