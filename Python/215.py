import itertools

# Project Euler problem 215: Crack Free Walls
rows = []

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
		rows.append(row)
		return

	# We only need a 3 x 1 brick, this is ok
	if sum(row) + 3 == max_width:
		row.append(3)
		rows.append(row)
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


def generate_solutions(max_height):
	# generate subsets of length max_height from rows
	return list(itertools.product(rows, repeat=max_height))
	

def count_solutions(w, h, m):
	generate_rows([], w)
	solutions = generate_solutions(h)
	count = 0
	for solution in solutions:
		if is_solution(solution):
			count += 1

	return count//2 % m


if __name__ == '__main__':
	# Test values
	print(count_solutions(9, 3, 1000))