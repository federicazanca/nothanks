from game_state import GameState, GameAction
from player_brain import DummyPlayerBrain

if __name__ == "__main__":
    brains = [DummyPlayerBrain() for _ in range(5)]
    game = GameState(brains)
    replay = GameState(brains, deck=game.deck)

    # Simulates the game and compute the incentives for training
    while True:
        if game.play() == None:
            break
    hpc = (len(game.players) - 1) / 2
    rankings = [(index, player.score()) for (index, player) in enumerate(game.players)]
    rankings.sort(key=lambda r: r[1], reverse=True)
    indices_with_incentives = [(r[0], float(i) - hpc)  for (i, r) in enumerate(rankings)]
    indices_with_incentives.sort(key=lambda r: r[0])
    incentives = [float(r[1]) for r in indices_with_incentives]

    # Trains the brains using the outcome of the game
    while True:
        active_player_index = game.active_player_index
        game_state = game.into_ml_matrix()
        outcome = replay.play()
        incentive = incentives[active_player_index]
        if outcome == None:
            break
        elif outcome == GameAction.FORCED:
            brains[active_player_index].train(game_state, 1.0, hpc + 1.0)
        elif outcome == GameAction.TAKE:
            brains[active_player_index].train(game_state, 1.0, incentive)
        elif outcome == GameAction.PASS:
            brains[active_player_index].train(game_state, 0.0, incentive)
