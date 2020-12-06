import numpy as np

def common_answers(groups):
	totalAnswers = 0
	questions = {}

	for group in groups:
		passengers = group.split("\n")
		for question in passengers[0]:
			if group.count(question) == len(passengers):
				questions[question] = True

		totalAnswers += len(questions)
		questions = {}

	return totalAnswers



# Example
answers = """abcx
abcy
abcz"""
groups = answers.split("\n\n")
print(common_answers(groups))

answers = """abc

a
b
c

ab
ac

a
a
a
a

b"""
groups = answers.split("\n\n")
print(common_answers(groups))

# My data
file = open('./input.data', 'r')
answers = file.read()[:-1]
groups = answers.split("\n\n")
print(common_answers(groups))
