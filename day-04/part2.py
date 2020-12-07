import numpy as np
import re

def validate_passports(passports):
	valid_passwords = 0
	completed_fields = []

	for line in passports:
		# End of current passport
		if line == "":
			if (len(completed_fields) == 7 and "cid" not in completed_fields) or (len(completed_fields) == 8):
				valid_passwords += 1
			completed_fields.clear()

		# Other line from current passport
		else:
			line_fields = [pair.split(":") for pair in line.split(" ")]
			for [field,value] in line_fields:
				if validate_field(field, value):
					completed_fields.append(field)

	return valid_passwords


def validate_field(field, value):
	if field == "byr":
		return 1920 <= int(value) <= 2002
	elif field == "iyr":
		return 2010 <= int(value) <= 2020
	elif field == "eyr":
		return 2020 <= int(value) <= 2030
	elif field == "hgt":
		[value, unit] = [value[:-2], value[-2:]]
		return ((unit == "cm") and (150 <= int(value) <= 193)) or \
			((unit == "in") and (59 <= int(value) <= 76))
	elif field == "hcl":
		return re.match("^#[0-9a-f]{6}$", value)
	elif field == "ecl":
		return value in ["amb","blu","brn","gry","grn","hzl","oth"]
	elif field == "pid":
		return len(value) == 9
	elif field == "cid":
		return True

	return False




# Example
passports = [
	"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
	"byr:1937 iyr:2017 cid:147 hgt:183cm",
	"",
	"iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
	"hcl:#cfa07d byr:1929",
	"",
	"hcl:#ae17e1 iyr:2013",
	"eyr:2024",
	"ecl:brn pid:760753108 byr:1931",
	"hgt:179cm",
	"",
	"hcl:#cfa07d eyr:2025 pid:166559648",
	"iyr:2011 ecl:brn hgt:59in",
	""
]
print(validate_passports(passports))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
passports = [line[:-1] for line in file.readlines()]
passports.append("")
print(validate_passports(passports))
