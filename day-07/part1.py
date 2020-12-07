import numpy as np

def search_colors_for_shiny_gold(rules):
	number_of_colors = 0

	# Get graph
	colors_graph = {}
	for rule in rules:
		[color, color_contain] = rule.split(" bags contain ")
		color_contain = [c[:c.find(" bag")].split(" ", 1) for c in color_contain[:-1].split(", ")]
		if color_contain == [['no', 'other']]:
			color_contain.clear()
		colors_graph[color] = color_contain

	# Calculate number of colors that shiny gold can contain
	for color in colors_graph:
		queue = [color]
		while queue != []:
			current_color = queue.pop(0)
			for [color_count, color_name] in colors_graph[current_color]:
				if color_name == "shiny gold":
					number_of_colors += 1
					queue.clear()
					break
				else:
					queue.append(color_name)

	return number_of_colors



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
print(search_colors_for_shiny_gold(rules))

# My data
print("Result for my puzzle:")
file = open('./input.data', 'r')
rules = file.read().split("\n")
print(search_colors_for_shiny_gold(rules))
