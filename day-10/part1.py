import numpy as np

def get_jolt_diffs(joltage_ratings, charging_outlet=0):
	jolt_diffs = {
		"1": 0,
		"2": 0,
		"3": 0
	}

	# List in ascendent order
	joltage_ratings.sort()

	previous_jolt = charging_outlet
	for jolt in joltage_ratings:
		jolt_diff = jolt - previous_jolt
		jolt_diffs[str(jolt_diff)] += 1
		previous_jolt = jolt

	jolt_diffs["3"] += 1

	return jolt_diffs


def get_solution(joltage_ratings, charging_outlet=0):
	jolt_diffs = get_jolt_diffs(joltage_ratings, charging_outlet)
	return jolt_diffs["1"] * jolt_diffs["3"]



# Example
data = """16
10
15
5
1
11
7
19
6
12
4""".split("\n")
data_int = [int(n) for n in data]
print(get_solution(data_int))

data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split("\n")
data_int = [int(n) for n in data]
print(get_solution(data_int))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
data_int = [int(n) for n in data]
print(get_solution(data_int))
