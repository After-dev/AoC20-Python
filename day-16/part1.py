import math
import numpy as np

def get_ticket_scanning_error_rate(data):
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

	# Search invalid values
	ticket_scanning_error_rate = 0
	for ticket in nearby_tickets:
		for n in ticket:
			if all(n not in ticket_rules[field] for field in ticket_rules):
				ticket_scanning_error_rate += n

	return ticket_scanning_error_rate




# Example
data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split("\n\n")
print(get_ticket_scanning_error_rate(data))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
data = file.read().split("\n\n")
print(get_ticket_scanning_error_rate(data))
