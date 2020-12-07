import numpy as np

def get_fast_seat_ID_1(boarding_passes):
	seats = list(range(1024))

	for boarding_pass in boarding_passes:
		rows = list(range(128))
		cols = list(range(8))

		for digit in boarding_pass:
			if digit == "F":
				rows = rows[:len(rows)//2]
			elif digit =="B":
				rows = rows[len(rows)//2:]
			elif digit == "R":
				cols = cols[len(cols)//2:]
			elif digit == "L":
				cols = cols[:len(cols)//2]

		site_ID = rows[0] * 8 + cols[0]
		seats[site_ID] = -1

	for seat in range(128, 1024-128):
		if (seats[seat] != -1) and (seats[seat+1] == -1) and (seats[seat-1] == -1):
			return seat

	return -1





def get_fast_seat_ID_2(boarding_passes):
	seats = list(range(1024))

	for boarding_pass in boarding_passes:
		row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
		col = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)

		site_ID = row * 8 + col
		seats[site_ID] = -1
	
	for seat in range(128, 1024-128):
		if (seats[seat] != -1) and (seats[seat+1] == -1) and (seats[seat-1] == -1):
			return seat

	return -1



# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
boarding_passes = [line[:-1] for line in file.readlines()]
print(get_fast_seat_ID_1(boarding_passes))
