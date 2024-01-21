import numpy as np
from typing import List, Tuple, Dict
from numpy import ndarray
from src.game.playerTokens import PlayerToken

#Logger
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def has_enough_pebbles(white_player_pebbles_taken: int, black_player_pebbles_taken: int) -> PlayerToken:
    if white_player_pebbles_taken >= 10:
        logger.info("Player White has won: 10 pebbles have been capture!")
        return PlayerToken.WHITE
    elif black_player_pebbles_taken >= 10:
        logger.info("Player Black has won: 10 pebbles have been capture!")
        return PlayerToken.BLACK
    else:
        return PlayerToken.EMPTY

def is_winning(game_state: ndarray, white_player_pebbles_taken: int, black_player_pebbles_taken: int, move_pos: Dict[str, int]) -> bool:
    if has_enough_pebbles(white_player_pebbles_taken, black_player_pebbles_taken) != PlayerToken.EMPTY:
        return True

    # Get row and column from move_pos dictionary
    row, col = move_pos["row"], move_pos["col"]
    pebble_color = game_state[row][col]

    # Define directions for checking: horizontal, vertical, and two diagonals
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for d_row, d_col in directions:
        count = 1  # Count includes the last placed pebble

        # Check in the positive direction
        for i in range(1, 5):
            r, c = row + i * d_row, col + i * d_col
            if 0 <= r < 19 and 0 <= c < 19 and game_state[r][c] == pebble_color:
                count += 1
            else:
                break

        # Check in the negative direction
        for i in range(1, 5):
            r, c = row - i * d_row, col - i * d_col
            if 0 <= r < 19 and 0 <= c < 19 and game_state[r][c] == pebble_color:
                count += 1
            else:
                break

        # Check if there are 5 in a row
        if count >= 5:
            # Assuming pebble_color is an instance of PlayerToken
            color_name = "Empty"
            if pebble_color == PlayerToken.BLACK.value:
                color_name = "Black"
            elif pebble_color == PlayerToken.WHITE.value:
                color_name = "White"

            logger.info(f"Player {color_name} has won: 5 pebbles are aligned!")
            return True

    # If no 5 in a row found, return False
    return False

# print(is_winning(game_state, 3, 7, {"row": 0, "col": 1}))