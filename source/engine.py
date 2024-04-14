from game_state import GameState
from player_brain import DummyPlayerBrain

if __name__ == "__main__":
    brains = [DummyPlayerBrain() for _ in range(5)]
    game = GameState(brains)
    replay = GameState(brains, deck=game.deck)

    # Simulates the game and rank the players(' indices)
    while True:
        if game.play() == None:
            break
    rankings = [(index, player.chips) for (index, player) in enumerate(game.players)]
    rankings.sort(key=lambda r: r[1])
    ranked_player_indices = [r[0] for r in rankings]

    # Trains the brains using the outcome of the game
    # TODO
