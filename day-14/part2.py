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
			pos = int(instruction[4:-1])
			pos_binary = format(pos, "b")
			memory_pos_mask = mask[:-len(pos_binary)]
			for digit in pos_binary:
				mask_digit = mask[len(memory_pos_mask)]
				memory_pos_mask += digit if mask_digit == "0" else mask_digit

			memory = assign_memory(memory, memory_pos_mask, int(value))

	return sum(memory.values())


def assign_memory(memory, pos, value):
	if pos.count("X") == 0:
		memory[int(pos, 2)] = value
	else:
		pos_X = pos.find("X")
		for i in ["0","1"]:
			pos = pos[:pos_X] + i + pos[pos_X+1:]
			memory = assign_memory(memory, pos, value)

	return memory




# Example
initialization_program = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split("\n")
print(get_solution(initialization_program))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
initialization_program = file.read().split("\n")
print(get_solution(initialization_program))
