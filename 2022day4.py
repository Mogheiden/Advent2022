day4 = open("2022day4.txt").readlines()
day4 = [line.strip() for line in day4]

part1_answer = 0
non_contain = []

for pair in day4:
	first, second = pair.split(',')
	first_index = first.index('-')
	second_index = second.index('-')

	first_upper = int(first[first_index + 1:])
	first_lower = int(first[:first_index])
	second_upper = int(second[second_index + 1:])
	second_lower = int(second[:second_index])

	if first_upper >= second_upper and first_lower <= second_lower:
		part1_answer += 1
		continue

	if first_upper <= second_upper and first_lower >= second_lower:
		part1_answer += 1
		continue

	non_contain.append((first_lower,first_upper,second_lower,second_upper))

print(part1_answer)

part2_answer = part1_answer

for i in non_contain:
	first_range = range(i[0], i[1] + 1)
	second_range = range(i[2], i[3] + 1)

	first_set = set(first_range)
	intersection = first_set.intersection(second_range)

	if len(intersection) > 0:
		part2_answer += 1


print(part2_answer)

for i in reversed(range(10)):
	print(i)