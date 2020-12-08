import numpy as np

def run_boot_code(boot_code):
	for line in range(len(boot_code)):
		[line_instruction, line_value] = boot_code[line].split(" ")

		if (line_instruction == "jmp") or (line_instruction == "nop"):
			# Change instructions jmp --> nop and nop --> jmp, one-by-one
			if line_instruction == "jmp":
				boot_code[line] = "nop "+line_value
			elif line_instruction == "nop":
				boot_code[line] = "jmp "+line_value

			# Verify modified code
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

				if pointer >= len(boot_code):
					return accumulator

			# Turn back the line. It's not the solution
			boot_code[line] = line_instruction+" "+line_value

	return -1



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
