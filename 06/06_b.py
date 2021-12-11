from sys import argv
import math

fishies = None
nfish = None

if len(argv) != 3:
	print(f"Usage: {argv[0]} <filename>")
	exit(1)

with open(argv[1], 'r') as f:
	for line in f:
		decrep = "".join(line.split(',')).strip()
		fishies = [int(n) for n in decrep]
		nfish = [1 for n in decrep]

print(f"Initial state: {''.join([str(n) for n in fishies])}")
print(f"Initial fish: {sum(nfish)}")

for i in range(1,int(argv[2]) + 1):
	newfish = 0
	for ifishes, fishes in enumerate(fishies):
		if fishes == 0:
			fishies[ifishes] = 6
			newfish = newfish + nfish[ifishes]
		else:
			fishies[ifishes] = fishes - 1

	if newfish > 0:
		fishies.append(8)
		nfish.append(newfish)
	# print(f"After {i} days: {''.join([str(fish)*nfish[ifish] for ifish, fish in enumerate(fishies)])}")

# print(f"Final state: {''.join([str(fish)*nfish[ifish] for ifish, fish in enumerate(fishies)])}")
print(f"Final count: {sum([n for n in nfish])}")