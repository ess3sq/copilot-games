# We want to implement a quiz game.
# The user will be asked a question and will be given a choice of answers.
# The user will be asked to select the correct answer.

def ask_question(question, answers):
	"""
	Prints a question and the answers to it.
	The user will be asked to select the correct answer.
	"""
	print(question)
	for i, answer in enumerate(answers):
		print(f"{i + 1}. {answer}")
	correct_answer = int(input("Select the correct answer: "))
	return correct_answer

def quiz(questions, all_answers):
	"""
	Takes a list of questions and answers and runs the quiz.
	"""
	score = 0
	for question, answers in zip(questions, all_answers):
		correct_answer = ask_question(question, answers)
		if correct_answer == 1:
			score += 1

	percentage = score / len(questions) * 100
	print(f"You got {score} out of {len(questions)} correct ({round(percentage)} %).")

def main():
	"""
	Runs the quiz. The questions and answers reside within the file questions.txt.
	The format is the following:

		Question 1
		Answer 1
		Answer 2
		Answer 3
		Answer 4
		Question 2
		Answer 1
		Answer 2
		Answer 3
		Answer 4
	"""
	# Read in the file with the format above.
	with open("questions.txt", "r") as file:
		questions = []
		answers = []
		current = None
		for line in file:
			if line.startswith("Question"):
				if current != None:
					answers.append(current)
				questions.append(line.strip())
				current = []
			else:
				current.append(line.strip())

		# Add the last question.
		answers.append(current)

		quiz(questions, answers)

if __name__ == "__main__":
	main()