from src.game.playerTokens import PlayerToken

def is_possible(self, pos: dict) -> bool:
    """Check if a move is possible."""
    if pos['row'] < 0 or pos['row'] >= self.board_size:
        return False
    if pos['col'] < 0 or pos['col'] >= self.board_size:
        return False
    if self.board[pos['col']][pos['row']] != 0:
        return False

    self.board[pos['col']][pos['row']] = self.current_player.value

    # Define directions for checking: horizontal, vertical, and two diagonals
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    nbr_of_free_tree = 0

    for direction in directions:
        if check_free_tree(self, pos, direction):
            nbr_of_free_tree += 1

    self.board[pos['col']][pos['row']] = PlayerToken.EMPTY
    if nbr_of_free_tree > 1:
        return False
    return True

def check_free_tree(self, pos: dict, direction: tuple):
    nbr_align_pebble = 0
    nbr_free_tree = 0

    # Check in the positive direction
    for i in range(1, 3):
        r, c = pos['row'] + i * direction[0], pos['col'] + i * direction[1]
        if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[pos['col']][pos['row']] == self.current_player.value:
            nbr_align_pebble += 1
        else:
            if self.board[pos['col']][pos['row']] == PlayerToken.EMPTY.value:
              nbr_free_tree += 1
            break

    # Check in the negative direction
    for i in range(1, 3):
        r, c = pos['row'] - i * direction[0], pos['col'] - i * direction[1]
        if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[pos['col']][pos['row']] == self.current_player.value:
            nbr_align_pebble += 1
        else:
            if self.board[pos['col']][pos['row']] == PlayerToken.EMPTY.value:
                nbr_free_tree += 1
            break

    if nbr_align_pebble == 3 and nbr_free_tree > 0:
        return True
    return False
