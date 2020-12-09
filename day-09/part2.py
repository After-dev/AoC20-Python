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

def XMAS_find_encription_weakness(preamble_size, data):
	invalid_value = XMAS_first_invalid(preamble_size, data)

	continuous_set = data[:2]
	for value in data[2:]:
		if np.sum(continuous_set) == invalid_value:
			break

		continuous_set.append(value)
		while np.sum(continuous_set) > invalid_value:
			continuous_set.pop(0)

	if np.sum(continuous_set) != invalid_value:
		return -1
	return np.min(continuous_set)+np.max(continuous_set)





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
print(XMAS_find_encription_weakness(5, data_int))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
data_int = [int(n) for n in data]
print(XMAS_find_encription_weakness(25, data_int))
