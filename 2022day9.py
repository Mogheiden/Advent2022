day9 = open("2022day9.txt").readlines()
day9 = [line.strip() for line in day9]

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
tail_visited = set((0,0))

for line in day9:
	direction, distance = line.split(' ')
	distance = int(distance)

	for i in range(distance):

		prev_head_x = head_x
		prev_head_y = head_y

		if direction == 'U':
			head_y += 1
		if direction == 'D':
			head_y -= 1
		if direction == 'R':
			head_x += 1
		if direction == 'L':
			head_x -= 1

		x_offset = head_x - tail_x
		y_offset = head_y - tail_y

		if abs(x_offset) > 1 or abs(y_offset) > 1:
			tail_x, tail_y = prev_head_x, prev_head_y
			tail_visited.add((tail_x, tail_y))

answer_1 = len(tail_visited)

# print(tail_visited)

print(answer_1)

knot_end_visited = set()

knot_chain = []

for i in range(10):
	knot_chain.append([0,0])

for line in day9:
	direction, distance = line.split(' ')
	distance = int(distance)

	for i in range(distance):

		if direction == 'U':
			knot_chain[0][0] += 1
		if direction == 'D':
			knot_chain[0][0] -= 1
		if direction == 'R':
			knot_chain[0][1] += 1
		if direction == 'L':
			knot_chain[0][1] -= 1

		for i in range(1,10):
			x_offset = knot_chain[i - 1][0] - knot_chain[i][0]
			y_offset = knot_chain[i - 1][1] - knot_chain[i][1]

			if x_offset != 0:
				x_offset -= 1 if x_offset > 0 else -1

			if y_offset != 0:
				y_offset -= 1 if y_offset > 0 else -1

			if x_offset or y_offset:
				knot_chain[i] = [knot_chain[i - 1][0] - x_offset, knot_chain[i - 1][1] - y_offset]


		knot_end_visited.add((knot_chain[-1][0], knot_chain[-1][1]))

print(len(knot_end_visited))
# print(knot_end_visited)



