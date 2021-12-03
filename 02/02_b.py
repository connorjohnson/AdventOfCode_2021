from sys import argv

pos = [0, 0, 0]

def sum_vec(vec1, vec2):
	assert(len(vec1) == len(vec2))
	return [ vec1[i] + vec2[i] for i in range(len(vec1)) ]

def mult_vec(vec, factor):
	return [ vec[i] * factor for i in range(len(vec)) ]

def parse_command(pos, command, val):
	if command == "down":
		pos = sum_vec(pos, [0, 0, val])
	elif command == "up":
		pos = sum_vec(pos, [0, 0, -val])
	elif command == "forward":
		pos = sum_vec(pos, [val, pos[2] * val, 0])
	else:
		abort(f"Command: {command} not defined.")

	return pos

def Usage():
	print(f"Usage: {argv[0]} <filename>")
	exit(1)

assert(len(argv) == 2)

with open(argv[1]) as file:
	for line in file:
		command, val = line.split(" ")
		print(pos)
		pos = parse_command(pos, command, int(val))

print(pos)
print(pos[0] * pos[1])
