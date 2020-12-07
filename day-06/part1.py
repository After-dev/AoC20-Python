import numpy as np

def distinct_answers(groups):
	totalAnswers = 0
	questions = {}

	for group in groups:
		for question in group:
			questions[question] = True

		totalAnswers += len(questions)
		questions = {}

	return totalAnswers



# Example
answers = """abcx
abcy
abcz"""
groups = answers.replace("\n\n", "\r").replace("\n", "").split("\r")
print(distinct_answers(groups))

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
groups = answers.replace("\n\n", "\r").replace("\n", "").split("\r")
print(distinct_answers(groups))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
answers = file.read()
groups = answers.replace("\n\n", "\r").replace("\n", "").split("\r")
print(distinct_answers(groups))
