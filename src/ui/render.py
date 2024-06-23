import matplotlib
# import tkinter
# matplotlib.use('TkAgg')  # Use the TkAgg backend to prevent segmentation fault

import matplotlib.pyplot as plt
import numpy as np

from src.game.playerTokens import PlayerToken


def plot_gomoku_board_interactive_with_player_info(gomoku):
	"""
	Plots an interactive Gomoku board with a title and player move info, based on the current game state.
	Handles user moves by capturing mouse click events and returns the updated game state.

	:return: Updated game state after each click.
	"""

	def draw_game_state():
		ax.clear()  # Clear existing stones
		ax.grid(which='both')
		ax.set_xlim(-0.5, 18.5)
		ax.set_ylim(-0.5, 18.5)
		ax.invert_yaxis()
		ax.set_aspect('equal', adjustable='box')
		ax.set_xticks(range(19))
		ax.set_yticks(range(19))
		next_player = "Black" if gomoku.current_player == PlayerToken.WHITE.value else "White"
		ax.set_title("Gomoku Game- Next Player: " + next_player, fontsize=14)
		ax.text(19.5, 9, f'Black Points: {gomoku.black_player_pebbles_taken}', verticalalignment='center')
		ax.text(19.5, 10, f'White Points: {gomoku.white_player_pebbles_taken}', verticalalignment='center')

		# Redraw each stone in the game state
		for row in range(19):
			for col in range(19):
				if gomoku.board[row, col] == 1:
					ax.scatter(col, row, s=200, color='white', edgecolors='black', zorder=2)
				elif gomoku.board[row, col] == -1:
					ax.scatter(col, row, s=200, color='black', edgecolors='black', zorder=2)

		plt.draw()

	def onclick(event):
		if event.xdata is not None and event.ydata is not None:
			col, row = int(round(event.xdata)), int(round(event.ydata))
			print(f"Col: {col}, Row: {row}")

			if gomoku.board[row, col] == PlayerToken.EMPTY.value:
				#Check if the move is forced
				if gomoku.forced_moves:
					if (row, col) not in gomoku.forced_moves:
						print("Invalid move")
						print(f"Valid moves are {gomoku.forced_moves}")
						return

				# Update the game state
				gomoku.board[row, col] = gomoku.current_player
				gomoku.check_capture_and_update({"row": row, "col": col})

				if gomoku.is_move_forbidden ({"row": row, "col": col}):
					print("Forbidden move: double three")
					return
				draw_game_state()


				# Check if the game is over
				if gomoku.is_win({"row": row, "col": col}):
					curret_player_name = "White" if gomoku.current_player == PlayerToken.WHITE.value else "Black"
					ax.set_title(f"{curret_player_name} has won the game!", fontsize=14)
					plt.draw()
					#remove the click event
					fig.canvas.mpl_disconnect(cid)
					return

				# Switch the player
				gomoku.current_player = -gomoku.current_player

	
		#TODO ADD Coup algo ici a terme. Pour le moment cest 1 vs 1

	# Setting up the plot
	fig, ax = plt.subplots(figsize=(10, 8))  # Slightly wider figure to accommodate labels
	ax.set_title("Gomoku Game, black starts", fontsize=14)
	ax.text(19.5, 9, f'Black Points: {gomoku.black_player_pebbles_taken}', verticalalignment='center')
	ax.text(19.5, 10, f'White Points: {gomoku.white_player_pebbles_taken}', verticalalignment='center')
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