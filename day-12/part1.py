import numpy as np

def get_Manhattan_distance(instructions):
	current_pos = [0,0]
	rotation_degrees = 0
	for i in instructions:
		if i[0] == "N":
			current_pos = move_ship(current_pos, 1, -i[1])
		elif i[0] == "S":
			current_pos = move_ship(current_pos, 1, i[1])
		elif i[0] == "E":
			current_pos = move_ship(current_pos, 0, i[1])
		elif i[0] == "W":
			current_pos = move_ship(current_pos, 0, -i[1])
		elif (i[0] == "L") or (i[0] == "R"):
			rotation_degrees = rotate_ship(rotation_degrees, i[0], i[1])
		elif i[0] == "F":
			if rotation_degrees == 0:
				current_pos = move_ship(current_pos, 0, i[1])
			elif rotation_degrees == 90:
				current_pos = move_ship(current_pos, 1, -i[1])
			elif rotation_degrees == 180:
				current_pos = move_ship(current_pos, 0, -i[1])
			elif rotation_degrees == 270:
				current_pos = move_ship(current_pos, 1, i[1])

	return sum([abs(i) for i in current_pos])


def move_ship(current_pos, axis, value):
	current_pos[axis] += value
	return current_pos

def rotate_ship(rotation_degrees, direction, value):
	if direction == "R":
		value *= -1
	return (rotation_degrees+value)%360




# Example
data = """F10
N3
F7
R90
F11""".split("\n")
instructions = [[line[0], int(line[1:])] for line in data]
print(get_Manhattan_distance(instructions))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
instructions = [[line[0], int(line[1:])] for line in data]
print(get_Manhattan_distance(instructions))
