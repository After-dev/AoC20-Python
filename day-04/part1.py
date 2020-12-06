import numpy as np

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
			line_fields = [pair.split(":")[0] for pair in line.split(" ")]
			for field in line_fields:
				completed_fields.append(field)

	return valid_passwords



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
file = open('./input.data', 'r')
passports = [line[:-1] for line in file.readlines()]
passports.append("")
print(validate_passports(passports))
