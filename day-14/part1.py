import math
import numpy as np

def get_solution(initialization_program):
	memory = {}

	# Calculate each memory value
	for line in initialization_program:
		[instruction, value] = line.split(" = ")
		if instruction == "mask":
			mask = value
		else:
			pos = instruction[4:-1]
			
			value_binary = format(int(value), "b")
			memory_value = mask[:-len(value_binary)]
			for digit in value_binary:
				mask_digit = mask[len(memory_value)]
				memory_value += digit if mask_digit == "X" else mask_digit

			memory[pos] = int(memory_value.replace("X", "0"), 2)

	return sum(memory.values())




# Example
initialization_program = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split("\n")
print(get_solution(initialization_program))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
initialization_program = file.read().split("\n")
print(get_solution(initialization_program))
