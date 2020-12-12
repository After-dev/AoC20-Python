import numpy as np

def get_Manhattan_distance(instructions):
	pos_waypoint = [10,-1]
	pos_ship = [0,0]
	for i in instructions:
		if i[0] == "N":
			pos_waypoint = move_pos(pos_waypoint, 1, -i[1])
		elif i[0] == "S":
			pos_waypoint = move_pos(pos_waypoint, 1, i[1])
		elif i[0] == "E":
			pos_waypoint = move_pos(pos_waypoint, 0, i[1])
		elif i[0] == "W":
			pos_waypoint = move_pos(pos_waypoint, 0, -i[1])
		elif (i[0] == "L") or (i[0] == "R"):
			pos_waypoint = rotate_pos(pos_waypoint, i[0], i[1])
		elif i[0] == "F":
			pos_ship = move_pos(pos_ship, 0, pos_waypoint[0]*i[1])
			pos_ship = move_pos(pos_ship, 1, pos_waypoint[1]*i[1])

	return sum([abs(i) for i in pos_ship])


def move_pos(current_pos, axis, value):
	current_pos[axis] += value
	return current_pos

def rotate_pos(pos, direction, value):
	while value > 0:
		pos = [pos[1], pos[0]]
		if direction == "R":
			pos[0] *= -1
		else:
			pos[1] *= -1

		value -= 90

	return pos





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
