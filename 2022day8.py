day8 = open("2022day8.txt").readlines()
day8 = [line.strip() for line in day8]

tree_map = []

for line in day8:
	int_line = []
	for char in line:
		int_line.append(int(char))
	tree_map.append(int_line)
# print(tree_map)

# print(day8)

outer = len(tree_map) * 2 + len(tree_map[0]) * 2 - 4

visible_trees = outer


for i in range(1,len(tree_map) - 1):
	for j in range(1, len(tree_map[0]) - 1):
		tree_height = tree_map[i][j]
		sides_hidden = 0
		for west in range(j):
			if tree_height <= tree_map[i][west]:
				sides_hidden += 1
				break
		for east in range(j + 1,len(tree_map[i])):
			if tree_height <= tree_map[i][east]:
				sides_hidden += 1
				break
		for north in range(i):
			if tree_height <= tree_map[north][j]:
				sides_hidden += 1
				break
		for south in range(i + 1,len(tree_map)):
			if tree_height <= tree_map[south][j]:
				sides_hidden += 1
				break

		if sides_hidden < 4:
			visible_trees += 1

print(visible_trees)

max_score = 0

for i in range(1,len(tree_map) - 1):
	for j in range(1, len(tree_map[0]) - 1):
		tree_height = tree_map[i][j]
		w_score = 0
		e_score = 0
		n_score = 0
		s_score = 0
		for west in reversed(range(j)):
			if tree_height <= tree_map[i][west]:
				w_score += 1
				break
			else:
				w_score += 1
		for east in range(j + 1,len(tree_map[i])):
			if tree_height <= tree_map[i][east]:
				e_score += 1
				break
			else:
				e_score += 1
		for north in reversed(range(i)):
			if tree_height <= tree_map[north][j]:
				n_score += 1
				break
			else:
				n_score += 1
		for south in range(i + 1,len(tree_map)):
			if tree_height <= tree_map[south][j]:
				s_score += 1
				break
			else:
				s_score += 1
		scenic_score = n_score * w_score * e_score * s_score
		if scenic_score > max_score:
			max_score = scenic_score

print(max_score)