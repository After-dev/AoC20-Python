import numpy as np

def count_trees(base_map, slopes):
	sol = 1
	base_map_height = len(base_map)
	base_map_width = len(base_map[0])

	for slope in slopes:
		number_of_trees = 0
		current_pos = [0, 0]
		while(current_pos[1] < base_map_height):
			# Check current position
			if base_map[current_pos[1]][current_pos[0]] == "#":
				number_of_trees += 1

			# Update position
			current_pos = [
				(current_pos[0] + slope[0]) % base_map_width,
				current_pos[1] + slope[1]
			]

		sol *= number_of_trees

	return sol



# Example
slopes = [
	[1, 1],
	[3, 1],
	[5, 1],
	[7, 1],
	[1, 2]
]
base_map = [
	"..##.......",
	"#...#...#..",
	".#....#..#.",
	"..#.#...#.#",
	".#...##..#.",
	"..#.##.....",
	".#.#.#....#",
	".#........#",
	"#.##...#...",
	"#...##....#",
	".#..#...#.#"
]
print(count_trees(base_map, slopes))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
base_map = [line[:-1] for line in file.readlines()]
print(count_trees(base_map, slopes))
