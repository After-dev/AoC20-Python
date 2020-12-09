import numpy as np

def XMAS_first_invalid(preamble_size, data):
	preamble = data[:preamble_size]
	for value in data[preamble_size:]:
		valid_value = False
		for v1 in preamble:
			for v2 in preamble:
				if (v1 != v2) and (v1+v2==value):
					valid_value = True

		if not valid_value:
			return value
		else:
			preamble.pop(0)
			preamble.append(value)

	return -1




# Example
data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")
data_int = [int(n) for n in data]
print(XMAS_first_invalid(5, data_int))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
data_int = [int(n) for n in data]
print(XMAS_first_invalid(25, data_int))
