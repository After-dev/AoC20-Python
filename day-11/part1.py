import numpy as np

def get_occupied_sites(seat_layout):
	changed = True
	occupied_sites = 0

	# do steps until there are no changes
	while(changed):
		changed = False
		new_seat_layout = []
		
		for row in range(len(seat_layout)):
			new_seat_layout.append([])
			for col in range(len(seat_layout[0])):
				new_seat_layout[-1].append(seat_layout[row][col])
				if (seat_layout[row][col] != "."):
					occupied_sites_adjacent = 0
					for [i,j] in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
						if (0 <= row+i < len(seat_layout)) and \
								(0 <= col+j < len(seat_layout[0])) and \
								(seat_layout[row+i][col+j] == "#"):
							occupied_sites_adjacent += 1

					if (seat_layout[row][col] == "L") and (occupied_sites_adjacent == 0):
						changed = True
						new_seat_layout[row][col] = "#"
						occupied_sites += 1
					elif (seat_layout[row][col] == "#") and (occupied_sites_adjacent >= 4):
						changed = True
						new_seat_layout[row][col] = "L"
						occupied_sites -= 1

		seat_layout = new_seat_layout

	return occupied_sites


# Example
data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split("\n")
seat_layout = [[c for c in line] for line in data]
print(get_occupied_sites(seat_layout))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n")
seat_layout = [[c for c in line] for line in data]
print(get_occupied_sites(seat_layout))
