from sys import argv

fishies = []

if len(argv) != 3:
	print(f"Usage: {argv[0]} <filename>")
	exit(1)

with open(argv[1], 'r') as f:
	for line in f:
		fishies.extend([int(n) for n in line.split(',')])

# initfishies = ","

def str_fishies(fishies):
	return ','.join([str(n) for n in fishies])

print(f"Initial state: {str_fishies(fishies)}")

for i in range(1,int(argv[2]) + 1):
	fish_to_append = 0
	for ifish, fish in enumerate(fishies):
		if fish == 0:
			fishies[ifish] = 6
			fish_to_append = fish_to_append + 1
		else:
			fishies[ifish] = fish-1
	fishies.extend([8 for fish in range(fish_to_append)])
	# print(f"After {i} days: {str_fishies(fishies)}")

print(f"Final state: {len(fishies)} fish.")