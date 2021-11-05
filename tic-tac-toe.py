# We want to implement a tic-tac-toe game.
# The game is played on a 3x3 board.
# The board is represented as a 3x3 matrix, where the value in each cell can be either 'X', 'O', or ' ' (space).
# A player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

# We start by adding the game loop:

# pretty print the board
def print_board(board):
	for row in board:
		line = " | ".join(row) 
		print("   " + line)
		print("  " + "-" * (len(line) + 2))

# Function that maps a number between 1 and 9 to a tuple of coordinates:
def map_number_to_coordinates(number):
	if number == 1:
		return (1, 1)
	elif number == 2:
		return (1, 2)
	elif number == 3:
		return (1, 3)
	elif number == 4:
		return (2, 1)
	elif number == 5:
		return (2, 2)
	elif number == 6:
		return (2, 3)
	elif number == 7:
		return (3, 1)
	elif number == 8:
		return (3, 2)
	elif number == 9:
		return (3, 3)
	else:
		print("[Error] Invalid number.")

def game():
	board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	# current player can be 1 or 2:
	current_player = '1'
	
	while True:
		# game loop
		print("[Current board]")
		print_board(board)

		# get player input as a number from 1 to 9
		player_input = int(input(f"[Player {current_player}] Please enter a number from 1 to 9: "))
		player_input = map_number_to_coordinates(player_input)

		# check if the input is valid
		if player_input == None:
			continue

		# check if input corresponds to a free cell in the board:
		if board[int(player_input[0]) - 1][int(player_input[1]) - 1] == ' ':
			board[int(player_input[0]) - 1][int(player_input[1]) - 1] = ('X' if current_player == '1' else 'O')
		else:
			print("[Error] This cell is already occupied.")
			continue

		# check if the game is over:
		if board[0][0] == board[0][1] == board[0][2] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		elif board[1][0] == board[1][1] == board[1][2] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		elif board[2][0] == board[2][1] == board[2][2] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		elif board[0][0] == board[1][0] == board[2][0] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		elif board[0][1] == board[1][1] == board[2][1] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		elif board[0][2] == board[1][2] == board[2][2] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		elif board[0][0] == board[1][1] == board[2][2] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		elif board[0][2] == board[1][1] == board[2][0] != ' ':
			print(f"[Game over] Player {current_player} wins!".format(current_player = current_player))
			break
		else:
			# check if the game is a draw:
			if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
				print("[Game over] The game is a draw.")
				break
			else:
				# switch players:
				current_player = '2' if current_player == '1' else '1'
		
	# Ask if the player wants to play again:
	play_again = input("[Play again?] (y/n): ")
	if play_again == 'y':
		game()



if __name__ == '__main__':
	game()