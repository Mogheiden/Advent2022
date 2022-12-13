from collections import defaultdict
MAX, need = 70000000, 30000000
limit = 100000

data = open("2022day7.txt").read().splitlines()
graph = defaultdict(list)
mp = defaultdict(int)
st = []
for command in data:
	command = command.split()
	if command[0] == '$':
		if command[1] == 'ls':
			continue
		elif command[2] == '..':
			st.pop(-1)
		else:
			st.append('.'.join(st + [command[2]]))
	else:
		if command[0] == 'dir':
			graph[st[-1]].append('.'.join(st + [command[1]]))
		else:
			mp[st[-1]] += int(command[0])

def dfs(node):
	for x in graph[node]:
		mp[node] += dfs(x)
	return mp[node]

# print(graph)
# print(mp)


dfs('/')

# Part 1
res1 = 0
for x, y in mp.items():
	if y <= limit:
		res1 += y

print(res1)

# Part 2
tot = mp['/']
res2 = float('inf')
for y in mp.values():
	if MAX - tot + y >= need:
		res2 = min(res2, y)

print(res2)

# print(res1, res2, sep = '\n')