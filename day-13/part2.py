import math
import numpy as np

def get_solution(bus_IDs):
	bus_IDs_int = [int(n) for n in list(filter(lambda a: a != "x", bus_IDs))]
	bus_IDs_offset = [bus_IDs.index(str(ID)) for ID in bus_IDs_int]

	M = 1
	for ID in bus_IDs_int:
		M *= ID

	t = 0
	for i in range(len(bus_IDs_int)):
		a = -bus_IDs_offset[i]
		b = M // bus_IDs_int[i]

		y = b % bus_IDs_int[i]
		b_inverse = 1
		while(True):
			if (y*b_inverse) % bus_IDs_int[i] == 1:
				break
			b_inverse += 1

		t += (a*b*b_inverse)

	return t%M



# Example
data = """7,13,x,x,59,x,31,19"""
bus_IDs = data.split(",")
print(get_solution(bus_IDs))

data = """17,x,13,19"""
bus_IDs = data.split(",")
print(get_solution(bus_IDs))

data = """67,7,59,61"""
bus_IDs = data.split(",")
print(get_solution(bus_IDs))

data = """67,x,7,59,61"""
bus_IDs = data.split(",")
print(get_solution(bus_IDs))

data = """67,7,x,59,61"""
bus_IDs = data.split(",")
print(get_solution(bus_IDs))

data = """1789,37,47,1889"""
bus_IDs = data.split(",")
print(get_solution(bus_IDs))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
earliest_timestamp = int(data[0])
bus_IDs = data[1].split(",")
print(get_solution(bus_IDs))
