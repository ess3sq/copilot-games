# This project implements Hangman as a CLI game.

import random

def get_word():
	"""
	This function will return a random word from a list of words.
	"""
	# Load the list of words.
	with open("words.txt", "r") as file:
		words = file.read().splitlines()

	# Return a random word from the list.
	return random.choice(words)

def get_word_string(word, guesses):
	"""
	This function will return a string of the word with the correct guesses.
	"""
	# Initialize the string.
	string = ""

	# Loop through the word.
	for letter in word:
		# Check if the letter has been guessed.
		if letter in guesses:
			# Add the letter to the string.
			string += letter
		else:
			# Add a dash to the string.
			string += "-"

	# Return the string.
	return string

def print_status(word, guesses, lives):
	"""
	This function will print the game status.
	"""
	# Print the word.
	print("Word: " + get_word_string(word, guesses))

	# Print the number of lives left.
	print("Lives: " + str(lives))

def get_guess(guesses):
	"""
	This function will get the user's guess.
	"""
	# Get the user's guess.
	guess = input("------\nGuess a letter: ")

	# Check if the user has already guessed the letter.
	if guess in guesses:
		print("You've already guessed that letter.")
		return get_guess(guesses)

	# Return the guess.
	return guess

def is_word_guessed(word, guesses):
	"""
	This function will check if the user has guessed all of the letters in the word.
	"""
	# Loop through the word.
	for letter in word:
		# Check if the letter has been guessed.
		if letter not in guesses:
			# The user has not guessed the letter.
			return False

	# The user has guessed all of the letters.
	return True

def play_game():
	"""
	This function is the game loop.
	It will run until the user wins or loses.
	"""
	# Initialize the game.
	word = get_word()
	guesses = []
	lives = 10

	# Run the game loop.
	while lives > 0:
		# Print the game status.
		print_status(word, guesses, lives)

		# Get the user's guess.
		guess = get_guess(guesses)

		# Check if the user guessed correctly.
		if guess in word:
			print("Correct!")
		else:
			print("Incorrect.")
			lives -= 1

		# Add the guess to the list of guesses.
		guesses.append(guess)

		# Check if the user has won.
		if is_word_guessed(word, guesses):
			print("You win!")
			break

	# Check if the user has lost.
	if lives == 0:
		print("You lose! The word was: " + word)

	# Ask the user if they want to play again.
	play_again = input("Play again? (y/n): ")
	if play_again == "y":
		play_game()

if __name__ == "__main__":
	play_game()