import numpy as np

def get_jolt_diff_ways(joltage_ratings, charging_outlet=0):
	# List in ascendent order
	joltage_ratings.sort()

	counts = { charging_outlet: 1 }
	for jolt in joltage_ratings:
		current_ways = 0
		for i in [1,2,3]:
			key = jolt-i
			if key in counts:
				current_ways += counts[key]

		counts[jolt] = current_ways

	return counts[joltage_ratings[-1]]



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
print(get_jolt_diff_ways(data_int))

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
print(get_jolt_diff_ways(data_int))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
data_int = [int(n) for n in data]
print(get_jolt_diff_ways(data_int))
