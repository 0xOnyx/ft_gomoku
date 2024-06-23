import numpy as np

from src.game.gomoku import Gomoku
# from src.game.playerTokens import PlayerToken

from src.ui.render import plot_gomoku_board_interactive_with_player_info


def main():
    gomoku = Gomoku()

    # Plot the interactive board with player move info
    plot_gomoku_board_interactive_with_player_info(gomoku)


if __name__ == "__main__":
    main()