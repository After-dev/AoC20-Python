import math
import numpy as np

def memory_game(starting_numbers):
	# Initialize memory
	memory = {}
	for i,num in enumerate(starting_numbers):
		memory[num] = i + 1

	# Turns
	next_number = len(memory) - memory[starting_numbers[-1]]
	for turn in range(len(memory)+1, 30000000):
		current_number = next_number
		next_number = turn - memory[current_number] if current_number in memory else 0
		memory[current_number] = turn

	return next_number




# Example
starting_numbers = """0,3,6"""
starting_numbers_int = [int(n) for n in starting_numbers.split(",")]
print(memory_game(starting_numbers_int))

starting_numbers = """1,3,2"""
starting_numbers_int = [int(n) for n in starting_numbers.split(",")]
print(memory_game(starting_numbers_int))

starting_numbers = """2,1,3"""
starting_numbers_int = [int(n) for n in starting_numbers.split(",")]
print(memory_game(starting_numbers_int))

starting_numbers = """1,2,3"""
starting_numbers_int = [int(n) for n in starting_numbers.split(",")]
print(memory_game(starting_numbers_int))

starting_numbers = """2,3,1"""
starting_numbers_int = [int(n) for n in starting_numbers.split(",")]
print(memory_game(starting_numbers_int))

starting_numbers = """3,2,1"""
starting_numbers_int = [int(n) for n in starting_numbers.split(",")]
print(memory_game(starting_numbers_int))

starting_numbers = """3,1,2"""
starting_numbers_int = [int(n) for n in starting_numbers.split(",")]
print(memory_game(starting_numbers_int))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
starting_numbers_int = [int(n) for n in file.read().split(",")]
print(memory_game(starting_numbers_int))
