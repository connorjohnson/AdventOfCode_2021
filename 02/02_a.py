from sys import argv

pos = [0, 0]

m_command={"forward": [1, 0], "up": [0, -1], "down": [0, 1]}

def sum_vec(vec1, vec2):
	assert(len(vec1) == len(vec2))
	return [ vec1[i] + vec2[i] for i in range(len(vec1)) ]

def mult_vec(vec, factor):
	return [ vec[i] * factor for i in range(len(vec)) ]

def parse_command(command, val):
	if command not in m_command:
		abort(f"Command: {command} not defined.")

	return mult_vec(m_command[command], val)

def Usage():
	print(f"Usage: {argv[0]} <filename>")
	exit(1)

assert(len(argv) == 2)

with open(argv[1]) as file:
	for line in file:
		command, val = line.split(" ")
		pos = sum_vec(pos, parse_command(command, int(val)))

print(pos[0] * pos[1])
