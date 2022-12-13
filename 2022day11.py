day11 = open("2022day11.txt").readlines()
day11 = [line.strip() for line in day11]

monkey_no = 0
monkeys = dict()

for line in day11:

	if "Monkey" in line:
		monkey_no = int(line[7])
		monkeys[monkey_no] = [0]

	if "Starting items" in line:
		items_list = []
		line = line[16:]
		line = line.split(', ')
		for number in line:
			items_list.append(int(number))
		monkeys[monkey_no].append(items_list)

	if "Operation" in line:
		operation = []
		line = line.split(' ')
		operation.append(line[-2])
		operation.append(line[-1])
		monkeys[monkey_no].append(operation)

	if "Test" in line:
		line = line.split(' ')
		monkeys[monkey_no].append(int(line[-1]))

	if "true" in line:
		line = line.split(' ')
		monkeys[monkey_no].append(int(line[-1]))

	if "false" in line:
		line = line.split(' ')
		monkeys[monkey_no].append(int(line[-1]))

time_saver = 1

# class Monkeh:
# 	def __init__(self, number, items):
# 		self.number = number
# 		self.items = items
# 		self.operation = operation

# for i in range(6):
# 	current = monkeys[i]
# 	current.items *= current.operation

for i in range(len(monkeys)):
	time_saver = time_saver * monkeys[i][3]

for i in range(20):
	for j in range(len(monkeys)):
		operation_no = 0
		if monkeys[j][2][1] != 'old':
			operation_no = int(monkeys[j][2][1])
		test = monkeys[j][3]
		true = monkeys[j][4]
		false = monkeys[j][5]
		for item in monkeys[j][1]:
			if operation_no > 0:
				if monkeys[j][2][0] == "+":
					item += operation_no
				else:
					item = item * operation_no
			else:
				item = item * item

			if item % test != 0:
				monkeys[false][1].append(item)
			else:
				monkeys[true][1].append(item)

			item = item // 3

			monkeys[j][0] += 1

		monkeys[j][1] = []


business_list = []

for i in range(len(monkeys)):
	business_list.append(monkeys[i][0])

business_list.sort()

part1 = business_list[-2] * business_list[-1]

print(part1)

#Part 2

monkey_no = 0
monkeys = dict()

for line in day11:

	if "Monkey" in line:
		monkey_no = int(line[7])
		monkeys[monkey_no] = [0]

	if "Starting items" in line:
		items_list = []
		line = line[16:]
		line = line.split(', ')
		for number in line:
			items_list.append(int(number))
		monkeys[monkey_no].append(items_list)

	if "Operation" in line:
		operation = []
		line = line.split(' ')
		operation.append(line[-2])
		operation.append(line[-1])
		monkeys[monkey_no].append(operation)

	if "Test" in line:
		line = line.split(' ')
		monkeys[monkey_no].append(int(line[-1]))

	if "true" in line:
		line = line.split(' ')
		monkeys[monkey_no].append(int(line[-1]))

	if "false" in line:
		line = line.split(' ')
		monkeys[monkey_no].append(int(line[-1]))


for i in range(10000):
	for j in range(len(monkeys)):
		operation_no = 0
		if monkeys[j][2][1] != 'old':
			operation_no = int(monkeys[j][2][1])
		test = monkeys[j][3]
		true = monkeys[j][4]
		false = monkeys[j][5]
		for item in monkeys[j][1]:
			if operation_no > 0:
				if monkeys[j][2][0] == "+":
					item += operation_no
				else:
					item = item * operation_no
			else:
				item = item * item

			if item % test != 0:
				item = item % time_saver
				monkeys[false][1].append(item)
			else:
				item = item % time_saver
				monkeys[true][1].append(item)

			monkeys[j][0] += 1

		monkeys[j][1] = []


business_list = []

for i in range(len(monkeys)):
	business_list.append(monkeys[i][0])

business_list.sort()

part2 = business_list[-2] * business_list[-1]

print(part2)
