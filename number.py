# Create a number guessing game.
# The user has to guess a number between 1 and 10.
# The computer will tell the user if the guess is too high or too low.
# The user will have to guess 5 times.
# If the user guesses the number, the game will end.

def main():
	import random
	number = random.randint(1, 10)
	guess = 0
	count = 0
	while guess != number and count < 5:
		guess = int(input("Guess a number between 1 and 10: "))
		if guess < number:
			print("Too low!")
		elif guess > number:
			print("Too high!")
		count += 1
	if guess == number:
		print("You got it!")
	else:
		print("You lost!")

	# Ask if the user wants to play again.
	play_again = input("Do you want to play again? (y/n) ")
	if play_again == "y":
		main()

main()