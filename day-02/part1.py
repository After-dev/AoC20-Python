import numpy as np

def validate_passwords(passwords):
	valid_passwords = 0

	for entry in passwords:
		[policy, password] = entry.split(":")
		[policy_counts, policy_letter] = policy.split(" ")
		[policy_min, policy_max] = [int(n) for n in policy_counts.split("-")]

		count = password.count(policy_letter)
		if policy_min <= count <= policy_max:
			valid_passwords += 1

	return valid_passwords



# Example
passwords = [
	"1-3 a: abcde",
	"1-3 b: cdefg",
	"2-9 c: ccccccccc"
]
print(validate_passwords(passwords))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
passwords = [line[:-1] for line in file.readlines()]
print(validate_passwords(passwords))
