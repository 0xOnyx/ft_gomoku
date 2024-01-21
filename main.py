from src.game.gomoku import Gomoku
from src.game.playerTokens import PlayerToken


def run():
    game = Gomoku(19, 2, PlayerToken.BLACK)
    x, y = game.get_next_move()
    game.set_next_move({1, 1})



run()