import sys

def sum_triple(measurement, start):
	return sum(measurement[start:start+3])

measurements = []
if len(sys.argv) == 2:
	with open(sys.argv[1]) as file:
		for line in file:
			measurements.append(int(line.rstrip()))
elif len(sys.argv) == 1:
	val = input("Enter a series of measurements:")
	while(val and val != ""):
		measurements.append(val)
		val = input("")
else:
	#print(f"Usage: {sys.argv[0]} [filename]")
	exit(1)

	
increases = [i for i in range(len(measurements) - 2) if sum_triple(measurements, i+1) > sum_triple(measurements, i)]

print(increases)
print(len(increases))
	
exit(0)

