import matplotlib
# import tkinter
# matplotlib.use('TkAgg')  # Use the TkAgg backend to prevent segmentation fault

import matplotlib.pyplot as plt
import numpy as np

from src.game.move import is_winning
from src.game.capture import is_capture


def plot_gomoku_board_interactive_with_player_info(gomoku):
	"""
	Plots an interactive Gomoku board with a title and player move info, based on the current game state.
	Handles user moves by capturing mouse click events and returns the updated game state.

	:return: Updated game state after each click.
	"""
	fig, ax = plt.subplots(figsize=(10, 8))  # Slightly wider figure to accommodate labels


	# Create labels for captured pieces
	black_captured_label = ax.text(19.5, 9, f'Black Captured: {gomoku.black_player_pebbles_taken}', verticalalignment='center')
	white_captured_label = ax.text(19.5, 10, f'White Captured: {gomoku.white_player_pebbles_taken}', verticalalignment='center')

	def re_draw_game_state():
		title_name_cpy = ax.title.get_text()

		ax.clear()  # Clear existing stones
		ax.grid(which='both')
		ax.set_xlim(-0.5, 18.5)
		ax.set_ylim(-0.5, 18.5)
		ax.invert_yaxis()
		ax.set_aspect('equal', adjustable='box')
		ax.set_xticks(range(19))
		ax.set_yticks(range(19))
		ax.set_title(title_name_cpy, fontsize=14)
  		ax.text(19.5, 9, f'Black Captured: {gomoku.black_player_pebbles_taken}', verticalalignment='center')
		ax.text(19.5, 10, f'White Captured: {gomoku.white_player_pebbles_taken}', verticalalignment='center')

		# Redraw each stone in the game state
		for y in range(19):
			for x in range(19):
				if gomoku.board[y, x] == 1:
					ax.scatter(x, y, s=200, color='white', edgecolors='black', zorder=2)
				elif gomoku.board[y, x] == -1:
					ax.scatter(x, y, s=200, color='black', zorder=2)


	# Function to update the plot and title
	def update_plot(x, y, player):
		if player == 1:
			ax.scatter(x, y, s=200, color='white', edgecolors='black', zorder=2)
			ax.set_title("Gomoku Game - Black's Turn", fontsize=14)
		elif player == -1:
			ax.scatter(x, y, s=200, color='black', zorder=2)
			ax.set_title("Gomoku Game - White's Turn", fontsize=14)
		elif player == 0:
			re_draw_game_state()

		fig.canvas.draw()

	def onclick(event):
		if event.xdata is not None and event.ydata is not None:
			x, y = int(round(event.xdata)), int(round(event.ydata))

			if gomoku.board[y, x] == 0:
				turn = -1 if np.count_nonzero(gomoku.board) % 2 == 0 else 1
				gomoku.board[y, x] = turn

				#TODO ADD move check before updating plot
				update_plot(x, y, turn)

				# Check for captures and update plot
				capture_result = is_capture(gomoku.board, {"row": y, "col": x})
				if capture_result:
					print(f"Some pebbles have been capture")
	
					#Update gamestate
					stone1, stone2 = capture_result
					gomoku.board[stone1['row'], stone1['col']] = 0
					gomoku.board[stone2['row'], stone2['col']] = 0
	
					#Update pebble count
					if turn == -1:
						gomoku.white_player_pebbles_taken += 2  # Black player captured white stones
					else:
						gomoku.black_player_pebbles_taken += 2
      
					update_plot(stone1['col'], stone1['row'], 0)  # Update plot for removed stones
					update_plot(stone2['col'], stone2['row'], 0)
	

				# Check if the current move wins the game
				winner = "Black" if turn == -1 else "White"
				if is_winning(gomoku.board, gomoku.white_player_pebbles_taken, gomoku.black_player_pebbles_taken, {"row": y, "col": x}):
					title.set_text(f"Gomoku Game - {winner} Wins!")
					fig.canvas.draw()
					fig.canvas.mpl_disconnect(cid)  # Disconnect the click event
	
		#TODO ADD Coup algo ici a terme. Pour le moment cest 1 vs 1
 
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