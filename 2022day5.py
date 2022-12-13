day5 = open("2022day5.txt").readlines()
day5 = [line.strip() for line in day5]

crates = ["   J   BW",
"   T WFRZ",
"  QM JRWH",
" FLP RNZG",
"FMSQ MPSC",
"LVRVWPCPJ",
"MZVSSVQHM",
"WBHFLFJVB"]

instruction_list = []

for i in range(len(crates)):
    line_list = []
    for char in crates[i]:
        line_list.append(char)
    crates[i] = line_list

for instruction in day5:
    relevant = instruction[5:]
    numbers = relevant.replace(" from ", " ").replace(" to ", " ").split()
    instruction_list.append((int(numbers[0]),int(numbers[1]) - 1,int(numbers[2]) - 1))

sideways_crates = []

for i in range(len(crates[0])):
    column = []
    for j in reversed(range(len(crates))):
        column.append(crates[j][i])
    sideways_crates.append(column)

crates = sideways_crates

for i in range(len(crates)):
    if ' ' in crates[i]:
        empty = crates[i].index(" ")
        crates[i] = crates[i][:empty]


print(crates)

def crate_collector(number, origin):
    current_crates = []
    pc = 0
    while pc < number:
            top_crate = crates[origin][-1]
            crates[origin] = crates[origin][:-1]
            current_crates.append(top_crate)
            pc += 1
    return current_crates

# for i in range(len(instruction_list)):
#     number, origin, destination = instruction_list[i]
#     current_crates = crate_collector(number, origin)
#     crates[destination] += current_crates

# part1_answer = []

# print(''.join(part1_answer))
# for line in crates:
#     part1_answer.append(line[-1])


part2_answer = []

for i in range(len(instruction_list)):
    number, origin, destination = instruction_list[i]
    current_crates = crates[origin][-number:]
    crates[origin] = crates[origin][:-number]
    crates[destination] += current_crates

for line in crates:
    part2_answer.append(line[-1])

print(''.join(part2_answer))

