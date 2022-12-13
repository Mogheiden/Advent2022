def in_order(l1, l2):
	if isinstance(l1, int) and isinstance(l2, int):
		if l1 == l2:
			return None
		return l1 < l2

	if isinstance(l1, list) and isinstance(l2, list):
		for num1, num2 in zip(l1, l2):
			if (comparison := in_order(num1, num2)) is not None:
				return comparison
		return in_order(len(l1), len(l2))

	if isinstance(l1, int):
		return in_order([l1], l2)
	return in_order(l1, [l2])

text = open("2022day13.txt", "r").read()
pairs = [[eval(l) for l in pair.splitlines()]for pair in text.strip().split("\n\n")]

part1_answer = 0
num = 1

for pair in pairs:
	if in_order(pair[0], pair[1]):
		part1_answer += num
		num += 1
	else:
		num += 1

packets = []

for pair in pairs:
	for lst in pair:
		packets.append(lst)

pos_1 = 0
pos_2 = 0

for packet in packets:
	if in_order(packet, [[2]]):
		pos_1 += 1

for packet in packets:
	if in_order(packet, [[6]]):
		pos_2 += 1

pos_1 += 1
pos_2 += 2

print(pos_1 * pos_2)
print(part1_answer)