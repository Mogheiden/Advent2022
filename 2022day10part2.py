
day10 = open("2022day10.txt").readlines()
day10 = [line.strip() for line in day10]

cycle = 0
signal = 1
crt_monitor = []

for i in range(6):
	line = []
	for i in range(40):
		line.append(' ')
	crt_monitor.append(line)

crt_sprite = [0,1,2]

def position_finder (value):
	y_pos = value // len(crt_monitor[0])
	x_pos = value - len(crt_monitor[0]) * y_pos

	return(y_pos, x_pos)

def cycle_update (current_cycle):
	current_pixel = position_finder(current_cycle)

	if current_pixel[1] in crt_sprite:
		crt_monitor[current_pixel[0]][current_pixel[1]] = '#'

	return(current_cycle + 1)

for line in day10:
	if ' ' in line:
		command, value = line.split(' ')
		value = int(value)
		cycle = cycle_update(cycle)
		cycle = cycle_update(cycle)
		signal += value
		crt_sprite = [signal - 1, signal, signal + 1]

	else:
		cycle = cycle_update(cycle)

for line in crt_monitor:
	print(''.join(line))