import numpy as np

def find_entries(expense_report, sum_value=2020):
	for i in range(len(expense_report)):
		for j in range(i+1, len(expense_report)):
			if expense_report[i]+expense_report[j] < sum_value:
				for k in range(j+1, len(expense_report)):
					if expense_report[i]+expense_report[j]+expense_report[k] == sum_value:
						return expense_report[i]*expense_report[j]*expense_report[k]
	return None





# Example
expense_report = [
	1721, 979, 366, 299, 675, 1456
]
print(find_entries(expense_report))

# My data
file = open('./input.data', 'r')
expense_report = [int(line[:-1]) for line in file.readlines()]
print(find_entries(expense_report))
