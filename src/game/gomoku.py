from audioop import minmax

import numpy as np

from src.algo.possible import is_possible
from src.game.move import is_winning
from src.game.playerTokens import PlayerToken


class Gomoku:
    """Gomoku game class."""

    def __init__(self, board_size=19, depth=2, player = PlayerToken.BLACK):
        """Initialize Gomoku game."""
        super().__init__()
        self.board_size = board_size
        self.depth = depth
        self.board = np.zeros((board_size, board_size), dtype='int8')
        self.current_player = player
        self.white_player_pebbles_taken = 0
        self.black_player_pebbles_taken = 0

    def get_next_move(self) -> (int, int):
        """Get next move."""
        first_possible_move = np.argwhere(self.board == PlayerToken.EMPTY)
        move_choice = {0, 0}
        last_heuristic_value = 0
        for x, y in first_possible_move:
            heuristic_value = minmax(self, self.current_player, {'row': x, 'col': y},
                      self.depth, -100000, 100000, True)
            if heuristic_value > last_heuristic_value:
                last_heuristic_value = heuristic_value
                move_choice = {x, y}
        return move_choice

    def set_next_move(self, pos: dict):
        """Set next move."""
        self.board[pos['col']][pos['row']] = self.current_player.value
        self.current_player = PlayerToken.WHITE if self.current_player == PlayerToken.BLACK else PlayerToken.BLACK

    def is_game_over(self, pos: dict) -> bool:
        return not is_winning(self.board, self.white_player_pebbles_taken, self.black_player_pebbles_taken, pos)

    def is_possible(self, pos: dict) -> bool:
        return is_possible(pos, self.board, self.board_size)

    def evaluate(self):
        return 0