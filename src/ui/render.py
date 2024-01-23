import matplotlib.pyplot as plt
import numpy as np

from src.game.move import is_winning


def plot_gomoku_board_interactive_with_player_info(game_state, black_captured=0, white_captured=0):
	"""
	Plots an interactive Gomoku board with a title and player move info, based on the current game state.
	Handles user moves by capturing mouse click events and returns the updated game state.

	:param game_state: A 19x19 numpy array representing the Gomoku board.
					-1 for black, 1 for white, 0 for empty.
	:return: Updated game state after each click.
	"""
	fig, ax = plt.subplots(figsize=(10, 8))  # Slightly wider figure to accommodate labels
	title = ax.set_title("Gomoku Game - Black's Turn", fontsize=14)


	# Create labels for captured pieces
	black_captured_label = ax.text(19.5, 9, f'Black Captured: {black_captured}', verticalalignment='center')
	white_captured_label = ax.text(19.5, 10, f'White Captured: {white_captured}', verticalalignment='center')

	# Function to update the plot and title
	def update_plot(x, y, player):
		if player == 1:
			ax.scatter(x, y, s=200, color='white', edgecolors='black', zorder=2)
			title.set_text("Gomoku Game - Black's Turn")
		elif player == -1:
			ax.scatter(x, y, s=200, color='black', zorder=2)
			title.set_text("Gomoku Game - White's Turn")

		black_captured_label.set_text(f'Black Captured: {black_captured}')
		white_captured_label.set_text(f'White Captured: {white_captured}')

		fig.canvas.draw()

	# Event handler for mouse clicks
	def onclick(event):
		if event.xdata is not None and event.ydata is not None:
			x, y = int(round(event.xdata)), int(round(event.ydata))

			# Check if the cell is empty and update the game state
			if game_state[y, x] == 0:
				# Assuming alternating turns, we can count the number of non-zero elements to determine whose turn it is
				turn = -1 if np.count_nonzero(game_state) % 2 == 0 else 1
				game_state[y, x] = turn
				update_plot(x, y, turn)

				winner = "Black" if turn == -1 else "White"
				if is_winning(game_state, 4, 4, {"row": y, "col": x}):
					title.set_text(f"Gomoku Game - {winner} Wins!")
					fig.canvas.draw()
					fig.canvas.mpl_disconnect(cid)  # Disconnect the click event

	# Setting up the plot
	ax.grid(which='both')
	ax.set_xlim(-0.5, 18.5)
	ax.set_ylim(-0.5, 18.5)
	ax.invert_yaxis()
	ax.set_aspect('equal', adjustable='box')
	ax.set_xticks(range(19))
	ax.set_yticks(range(19)) 

	# Connect the click event
	cid = fig.canvas.mpl_connect('button_press_event', onclick)

	plt.show()