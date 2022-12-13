day12 = open("2022day12.txt").readlines()
day12 = [line.strip() for line in day12]

topography = []
start = (0,0)
finish = (1,1)

a_list = []
route_distances = []

for i in range(len(day12)):
	line = []
	for j in range(len(day12[i])):

		if day12[i][j] == "S":
			start = (j,i)
			line.append('a')

		elif day12[i][j] == "E":
			finish = (j,i)
			line.append("z")


		else:
			line.append(day12[i][j])

	topography.append(line)

distance_dict = {(start[0],start[1]): 0}
pending = [(start[0],start[1],0)]

while len(pending) > 0:
	x, y, distance = pending.pop(0)

	coordinate_list = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]

	for coord in coordinate_list:
		newx = coord[0]
		newy = coord[1]

		if coord in distance_dict:
			continue

		if coord[0] < 0 or coord[1] < 0:
			continue

		if coord[0] > len(topography[0]) - 1:
			continue

		if coord[1] > len(topography) - 1:
			continue

		if ord(topography[y][x]) - ord(topography[newy][newx]) >= - 1:
			distance_dict[coord] = distance + 1
			pending.append((newx, newy, distance + 1))

	pending.sort(key=lambda a: a[2])

part1_answer = (distance_dict[finish])
print(part1_answer)


back_distance_dict = {(finish[0],finish[1]): 0}
pending = [(finish[0],finish[1],0)]

while len(pending) > 0:
	x, y, distance = pending.pop(0)

	coordinate_list = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]

	for coord in coordinate_list:
		newx = coord[0]
		newy = coord[1]

		if coord in back_distance_dict:
			continue

		if coord[0] < 0 or coord[1] < 0:
			continue

		if coord[0] > len(topography[0]) - 1:
			continue

		if coord[1] > len(topography) - 1:
			continue

		if ord(topography[y][x]) <= ord(topography[newy][newx]) + 1:
			back_distance_dict[coord] = distance + 1
			if topography[newy][newx] == 'a':
				a_list.append(distance + 1)
			pending.append((newx, newy, distance + 1))

	pending.sort(key=lambda a: a[2])

part2_answer = min(a_list)
print(part2_answer)
