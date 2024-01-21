import numpy as np

from src.game.gomoku import Gomoku
from src.game.playerTokens import PlayerToken

from src.ui.render import plot_gomoku_board_interactive_with_player_info


def main():
	game_state = np.zeros((19, 19), dtype=int)

	# Plot the interactive board with player move info
	plot_gomoku_board_interactive_with_player_info(game_state)
 
 
if __name__ == "__main__":
	main()