day2 = open("2022day2.txt").readlines()
day2 = [line.strip() for line in day2]

for i in range(len(day2)):
	day2[i] = (day2[i][0], day2[i][2])

r_p_s = [1,2,3]

score = 0

for i in day2:
	if i[1] == 'X':
		score += 1
		if i[0] == 'A':
			score += 3
		elif i[0] == 'B':
			score += 0
		elif i[0] == 'C':
			score += 6
		else:
			print("error")
	if i[1] == 'Y':
		score += 2
		if i[0] == 'A':
			score += 6
		elif i[0] == 'B':
			score += 3
		elif i[0] == 'C':
			score += 0
		else:
			print("error")
	if i[1] == 'Z':
		score += 3
		if i[0] == 'A':
			score += 0
		elif i[0] == 'B':
			score += 6
		elif i[0] == 'C':
			score += 3
		else:
			print("error")

print(score)

score_2 = 0

for i in day2:
	if i[1] == 'X':
		score_2 += 0
		if i[0] == 'A':
			score_2 += 3
		elif i[0] == 'B':
			score_2 += 1
		elif i[0] == 'C':
			score_2 += 2
		else:
			print("error")
	if i[1] == 'Y':
		score_2 += 3
		if i[0] == 'A':
			score_2 += 1
		elif i[0] == 'B':
			score_2 += 2
		elif i[0] == 'C':
			score_2 += 3
		else:
			print("error")
	if i[1] == 'Z':
		score_2 += 6
		if i[0] == 'A':
			score_2 += 2
		elif i[0] == 'B':
			score_2 += 3
		elif i[0] == 'C':
			score_2 += 1
		else:
			print("error")

print(score_2)