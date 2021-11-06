# We want to play nim.
# We have a pyramid of stones.
# The player who takes the last stone loses.

class Pyramid:
	def __init__(self):
		self.pyramid = []
		# Each element of self.pyramid should be a list of stones.
		# The first list has 1 stone, the second has 3 stones, the third list has 5 stones and the last has 7.
		# Loop through the 4 lists and add them to self.pyramid.
		for i in range(0,4):
			# construct a list of 1 + 2*i elements all initialized to False
			self.pyramid.append([False]*(1+2*i))

	def check_win(self):
		# Check if every row in the pyramid contains only True values.
		# If so, return True.
		# If not, return False.
		for i in range(0,4):
			# Loop through the columns of the pyramid to achieve this:
			for j in range(0,2*i+1):
				# If any element in the row is False, return False
				if not self.pyramid[i][j]:
					return False
		# If no False values were found, return True
		return True

	def print(self):
		# Return a string representation of the pyramid.
		# It should look like this:
		#      I
		# 	 I I I
		#  I I I I I
		# I I I I I I I

		# The first line should be the first element of self.pyramid.
		# The second line should be the second element of self.pyramid.
		# The third line should be the third element of self.pyramid.
		# The fourth line should be the fourth element of self.pyramid.

		# Loop through rows of the pyramid to achieve this:
		for i in range(0,4):
			# Loop through the columns of the pyramid to achieve this:
			for j in range(0,2*i+1):
				# print I if the element at self.pyramid[i][j] is False, and X if True
				print('X' if self.pyramid[i][j] else 'I', end=" ")
			# print a newline
			print()

def game():
	# Create an object to represent the pyramid.
	pyramid = Pyramid()

	# Create player id. Player 1 starts:
	player = 1

	# Start game loop.
	# Loop until the player loses.
	while True:
		# Print pyramid and ask the player for a move.
		pyramid.print()

		# Check if the player has lost.
		if pyramid.check_win():
			# If so, print the appropriate message.
			print("Player", player, "loses!")
			break

		# Ask player for the row number and the number of sticks to cross:
		num_row = int(input(f"[Player {player}] Enter row number: "))
		num_sticks = int(input(f"[Player {player}] Enter number of sticks to cross: "))

		# Check if the player has made a valid move, aka. num_row is within 1 and 4 and num_sticks is > 0:
		if num_row < 1 or num_row > 4:
			# If not, print the appropriate message.
			print("Invalid row number.")
			continue

		if num_sticks < 1:
			# If not, print the appropriate message.
			print("Invalid number of sticks.")
			continue

		# Get the row:
		row = pyramid.pyramid[num_row-1]
		# If the player tries to cross more sticks than are in the row, print an error message and ask again.
		# This means check number of False elements within the row:
		if num_sticks > row.count(False):
			print("Invalid move!")
			continue
		# Otherwise, cross the sticks:
		crossed = 0
		success = True

		while crossed < num_sticks:
			# Find the first False element in the row, if it is not found, print an error message and ask again.
			try:
				index = row.index(False)
				# Set the element to True:
				row[index] = True
				# Increment crossed:
				crossed += 1
			except:
				print("Invalid move!")
				success = False
				break

		if not success:
			continue

		player = 3 - player

	# Ask the player if he wants to play again.
	# If so, call game() again.
	# If not, exit the program.
	play_again = input("Play again? (y/n): ")
	if play_again == "y":
		game()

if __name__ == "__main__":
	game()