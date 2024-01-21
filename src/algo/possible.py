from numpy import ndarray

def is_possible(pos: dict, board: ndarray, board_size: int ) -> bool:
    """Check if a move is possible."""
    if pos['row'] < 0 or pos['row'] >= board_size:
        return False
    if pos['col'] < 0 or pos['col'] >= board_size:
        return False
    if board[pos['col']][pos['row']] != 0:
        return False
    return True
