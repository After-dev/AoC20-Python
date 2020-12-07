import numpy as np

def shiny_gold_bags_required(rules):
	number_of_bags = {}

	# Get graph
	colors_graph = {}
	for rule in rules:
		[color, color_contain] = rule.split(" bags contain ")
		color_contain = [c[:c.find(" bag")].split(" ", 1) for c in color_contain[:-1].split(", ")]
		if color_contain == [['no', 'other']]:
			color_contain.clear()
		colors_graph[color] = color_contain

	# Calculate number of bags that each color can contain
	stack = list(colors_graph.keys())
	while stack != []:
		current_color = stack.pop(0)

		current_count = 0
		for [color_count, color_name] in colors_graph[current_color]:
			if color_name in number_of_bags:
				current_count += int(color_count) + int(color_count)*number_of_bags[color_name]
			else:
				current_count = None
				stack.append(current_color)
				break

		if current_count is not None:
			number_of_bags[current_color] = current_count

	return number_of_bags["shiny gold"]



# Example
rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")
print(shiny_gold_bags_required(rules))

rules = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split("\n")
print(shiny_gold_bags_required(rules))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
rules = file.read().split("\n")
print(shiny_gold_bags_required(rules))
