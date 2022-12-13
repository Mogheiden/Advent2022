day1 = open("2022day1.txt").readlines()
day1 = [line.strip() for line in day1]

elf_total = 0

totals_list = []

for i in day1:
	if i == '':
		totals_list.append(elf_total)
		elf_total = 0
	else:
		elf_total += int(i)

part1_answer = max(totals_list)


print(part1_answer)

totals_list.sort()

part2_answer = totals_list[-3] + totals_list[-2] + totals_list[-1]

print(part2_answer)