import numpy as np

def run_boot_code(boot_code):
	pointer = 0
	accumulator = 0
	executed_lines = {}

	while str(pointer) not in executed_lines:
		[instruction, value] = boot_code[pointer].split(" ")
		executed_lines[str(pointer)] = True
		if instruction == "acc":
			accumulator += int(value)
			pointer += 1
		elif instruction == "jmp":
			pointer += int(value)
		elif instruction == "nop":
			pointer += 1

	return accumulator



# Example
boot_code = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split("\n")
print(run_boot_code(boot_code))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
boot_code = file.read().split("\n")
print(run_boot_code(boot_code))
