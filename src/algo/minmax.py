from numpy import ndarray

from src.game.playerTokens import PlayerToken


def minmax(self, current_player: PlayerToken, current_pos: dict, depth: int, alpha: int, beta: int, maximizingPlayer: bool):
    if self.is_possible_move(current_pos):
        return -100000;
    self.board[current_pos['col']][current_pos['row']] = current_player.value
    if depth == 0 or self.is_game_over(current_pos):
        return self.evaluate()

    # if maximizingPlayer:
    #     maxEval = -math.inf
    #     bestMove = None
    #     for move in board.legal_moves:
    #         board.push(move)
    #         eval = minmax(board, depth - 1, alpha, beta, False)[0]
    #         board.pop()
    #         if eval > maxEval:
    #             maxEval = eval
    #             bestMove = move
    #         alpha = max(alpha, eval)
    #         if beta <= alpha:
    #             break
    #     return maxEval, bestMove
    # else:
    #     minEval = math.inf
    #     bestMove = None
    #     for move in board.legal_moves:
    #         board.push(move)
    #         eval = minmax(board, depth - 1, alpha, beta, True)[0]
    #         board.pop()
    #         if eval < minEval:
    #             minEval = eval
    #             bestMove = move
    #         beta = min(beta, eval)
    #         if beta <= alpha:
    #             break
    #     return minEval, bestMove