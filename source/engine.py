from game_state import GameState

if __name__ == "__main__":
    game = GameState()
    while True:
        if game.play():
            break
    # print(game.into_ml_matrix())
