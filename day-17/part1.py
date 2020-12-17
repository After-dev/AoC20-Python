import math
import numpy as np
from itertools import product

def simulation(initial_state, cycles):
	l = len(initial_state)
	cubes_ON = [(x,y,0) for x,y in product(range(l), range(l)) if initial_state[x][y] == "#"]

	for cycle in range(cycles):
		current_cubes_ON = []
		dim_cube = l + cycle
		for x in range(-dim_cube+l, dim_cube+1):
			for y in range(-dim_cube+l, dim_cube+1):
				for z in range(-cycle-1, cycle+2):
					n_cubes_ON = 0
					for dx,dy,dz in product([-1,0,1],[-1,0,1],[-1,0,1]):
						if (dx != 0) or (dy != 0) or (dz != 0):
							if (x+dx, y+dy, z+dz) in cubes_ON:
								n_cubes_ON += 1
					if ((x,y,z) not in cubes_ON) and (n_cubes_ON == 3):
						current_cubes_ON.append((x,y,z))
					if ((x,y,z) in cubes_ON) and (n_cubes_ON in [2,3]):
						current_cubes_ON.append((x,y,z))
		cubes_ON = current_cubes_ON

	return len(cubes_ON)




# Example
data = """.#.
..#
###""".split("\n")
initial_state = [[c for c in line] for line in data]
print(simulation(initial_state, 6))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
initial_state = [[c for c in line] for line in data]
print(simulation(initial_state, 6))
