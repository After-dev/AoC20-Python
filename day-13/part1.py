import math
import numpy as np

def get_solution(earliest_timestamp, bus_IDs):
	bus_timestamps = []
	for ID in bus_IDs:
		nearest_timestamp = math.ceil(earliest_timestamp/ID) * ID
		bus_timestamps.append(nearest_timestamp)

	earliest_bus = bus_timestamps.index(min(bus_timestamps))
	return (bus_timestamps[earliest_bus] - earliest_timestamp) * bus_IDs[earliest_bus]




# Example
data = """939
7,13,x,x,59,x,31,19""".split("\n")
earliest_timestamp = int(data[0])
bus_IDs = [int(n) for n in list(filter(lambda a: a != "x", data[1].split(",")))]
print(get_solution(earliest_timestamp, bus_IDs))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
earliest_timestamp = int(data[0])
bus_IDs = [int(n) for n in list(filter(lambda a: a != "x", data[1].split(",")))]
print(get_solution(earliest_timestamp, bus_IDs))
