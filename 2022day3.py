day3 = open("2022day3.txt").readlines()
day3 = [line.strip() for line in day3]

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

doubles = []
triples = []

pc = 0
score_2 = 0
score = 0

def split_list(a_list):
	half = len(a_list)//2
	return a_list[:half], a_list[half:]

day1_answer = 0

for i in range(len(day3)):
	first, second = split_list(day3[i])
	for j in first:
		if j in second:
			doubles.append(j)
			break

for char in doubles:
	score += int(priorities.index(char)) + 1

print(score)


while pc < len(day3):
	for i in day3[pc]:
		if i in day3[pc + 1]:
			if i in day3[pc + 2]:
				triples.append(i)
				print(i)
				pc += 3
				break

for char in triples:
	score_2 += int(priorities.index(char)) + 1

print(score_2)