import itertools

# Project Euler problem 215: Crack Free Walls
rows = []
s_dict = {}

def generate_rows(row, max_width):
	"""
	Generate all possible rows subject to max_width
	We only have (2,1) and (3,1) blocks
	"""
	global rows
	
	# As this is too short, we cannot accept this
	if sum(row) + 1 == max_width:
		return

	# We only need a 2 x 1 brick, this is ok
	if sum(row) + 2 == max_width:
		row.append(2)
		rows.append(tuple(row))
		return

	# We only need a 3 x 1 brick, this is ok
	if sum(row) + 3 == max_width:
		row.append(3)
		rows.append(tuple(row))
		return

	# Call generate_row recursively to generate all
	# possible permutations
	generate_rows(row + [2], max_width)
	generate_rows(row + [3], max_width)


def is_solution(possible_solution):
	"""
	Check if a particular row_combination is valid
	ie. no cracks

	:Example:

	Crack   Crack       Crack	
	|		|			|			|
	|		|			|		|
	"""
	# Compare between n and n + 1 row combination
	# If there is a matching sequence in the same place 
	# we reject
	# [..., 2, 2, 3, ...], [..., 2, 2, 3, ...]
	for i in range(len(possible_solution)):
		if i + 1 < len(possible_solution):
			row_1 = possible_solution[i]
			row_2 = possible_solution[i + 1]

			# if the first row equals, we should immediately 
			for j in range(min(len(row_1), len(row_2))):
				if sum(row_1[:j + 1]) == sum(row_2[:j + 1]):
					if j + 1 == min(len(row_1), len(row_2)):
						break
					else:
						return False
		# We've reached the end. If solution survived, it is valid
	return True


def generate_s_dict():
	global s_dict

	for row_key in rows:
		for row_val in rows:
			if is_solution([row_key] + [row_val]):
				try:
					s_dict[row_key] += [row_val] 
				except:
					s_dict[row_key] = [row_val]


def count_solutions(w, h, m):
	generate_rows([], w)
	generate_s_dict()

	def helper_recursion(key, h, count):
		if h == 2:
			return 1

		else:
			for key in s_dict[key]:
				count += helper_recursion(key, h - 1, count)

			return count

	count = 0
	for key in s_dict.keys():
		count += helper_recursion(key, h, 0)

	return count % m



if __name__ == '__main__':
	# Test values
	value1 = count_solutions(9, 3, 100)
	print(value1)
	print(value1 == 8)

	rows = []
	s_dict = {}
	value1 = count_solutions(32, 10, 10000)
	print(value1)
	print(value1 == 806844323190414)