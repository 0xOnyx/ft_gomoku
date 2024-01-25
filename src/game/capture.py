import numpy as np
from typing import List, Tuple, Dict, Union
from numpy import ndarray
from src.game.playerTokens import PlayerToken

def is_capture(game_state: ndarray, move_pos: Dict[str, int]) -> Union[Tuple[Dict[str, int], Dict[str, int]], bool]:
    # Get row and column from move_pos dictionary
    row, col = move_pos["row"], move_pos["col"]
    pebble_color = game_state[row][col]
    opponent_color = 1 if pebble_color == -1 else -1

    # Define directions for checking: horizontal, vertical, and two diagonals
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for d_row, d_col in directions:
        # Check in the positive direction
        if is_pair_captured(game_state, row, col, d_row, d_col, pebble_color, opponent_color):
            return (get_captured_position(row, col, d_row, d_col, 1),
                    get_captured_position(row, col, d_row, d_col, 2))

        # Check in the negative direction
        if is_pair_captured(game_state, row, col, -d_row, -d_col, pebble_color, opponent_color):
            return (get_captured_position(row, col, -d_row, -d_col, 1),
                    get_captured_position(row, col, -d_row, -d_col, 2))

    # If no capture found, return False
    return False

def is_pair_captured(game_state, row, col, d_row, d_col, pebble_color, opponent_color):
    # Check for exactly two consecutive opponent stones followed by a stone of the current player's color
    if all(0 <= row + i * d_row < 19 and 0 <= col + i * d_col < 19 and 
           game_state[row + i * d_row][col + i * d_col] == opponent_color for i in range(1, 3)) \
       and 0 <= row + 3 * d_row < 19 and 0 <= col + 3 * d_col < 19 and \
       game_state[row + 3 * d_row][col + 3 * d_col] == pebble_color:
        return True
    return False

def get_captured_position(row, col, d_row, d_col, distance):
    return {'row': row + distance * d_row, 'col': col + distance * d_col}
