import math
import numpy as np

def find_fields(data):
	# Parse rules
	ticket_rules = {}
	for rule in data[0].split("\n"):
		[field, ranges] = rule.split(": ")
		field_valid_values = []
		for r in ranges.split(" or "):
			[min_r, max_r] = r.split("-")
			field_valid_values += range(int(min_r), int(max_r)+1)
		ticket_rules[field] = field_valid_values

	# Parse my ticket
	my_ticket = [int(n) for n in data[1].split("\n")[1].split(",")]
	
	# Parse nearby tickets
	nearby_tickets = [[int(n) for n in ticket.split(",")] for ticket in data[2].split("\n")[1:]]

	# Remove invalid nearby tickets
	valid_nearby_tickets = []
	for ticket in nearby_tickets:
		valid = True
		for n in ticket:
			if all(n not in ticket_rules[field] for field in ticket_rules):
				valid = False
		if valid:
			valid_nearby_tickets.append(ticket)

	# Find possible fields
	possible_fields = {}
	for col in range(len(valid_nearby_tickets[0])):
		valid_fields = list(ticket_rules.keys())
		for ticket in range(len(valid_nearby_tickets)):
			for field in ticket_rules:
				if (field in valid_fields) and (valid_nearby_tickets[ticket][col] not in ticket_rules[field]):
					valid_fields.remove(field)
		possible_fields[col] = valid_fields

	allocated = {}
	while len(allocated) < len(possible_fields):
		for col in possible_fields:
			field = possible_fields[col][0]
			if (len(possible_fields[col]) == 1) and (field not in allocated):
				allocated[field] = col
				for col2 in possible_fields:
					if (col != col2) and (field in possible_fields[col2]):
						possible_fields[col2].remove(field)

	return np.prod([my_ticket[allocated[key]] for key in allocated if key.startswith("departure")])




# Example
data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".split("\n\n")
#print(find_fields(data))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n\n")
print(find_fields(data))
