from sys import argv

class Pos():
	def __init__(self, part):
		posstr = part.split(',')
		self.x = int(posstr[0])
		self.y = int(posstr[1])

def read_line(line):
	parts = line.split()
	assert(len(parts)) == 3
	return Pos(parts[0]), Pos(parts[2])

if len(argv) != 2:
	print(f"Usage: {argv[0]} <filename>")
	exit(1)

gridsize=[1000, 1000]

grid = []
for i in range(gridsize[0]):
	grid.append([])
	for j in range(gridsize[1]):
		grid[i].append(0)

with open(argv[1], 'r') as f:
	for line in f:
		formline = read_line(line)
		start,stop = read_line(line)
		if start.x == stop.x or start.y == stop.y:
			for i in range(min(start.x, stop.x), max(start.x, stop.x) + 1):
				for j in range(min(start.y, stop.y), max(start.y, stop.y) + 1):
					grid[j][i] = grid[j][i] + 1
		elif abs(start.x - stop.x) == abs(start.y - stop.y):
			dirx = 1 if start.x < stop.x else -1
			diry = 1 if start.y < stop.y else -1
			for i in range(abs(start.x - stop.x) + 1):
				grid[start.y + i*diry][start.x + i*dirx] = grid[start.y + i*diry][start.x + i*dirx] + 1 

def printgrid(grid):
	for row in grid:
		print(' '.join([str(col) for col in row]))

# printgrid(grid)

count = 0
for row in grid:
	count = count + len([e for e in row if e > 1])
print(f"Total intersections: {count}")
