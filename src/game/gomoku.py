import numpy as np

from src.game.playerTokens import PlayerToken


class Gomoku:
    """Gomoku game class."""

    def __init__(self, board_size=19, depth=2, player = PlayerToken.BLACK):
        """Initialize Gomoku game."""
        super().__init__()
        self.board_size = board_size
        self.depth = depth
        self.board = np.zeros((board_size, board_size),)
        self.current_player = player
