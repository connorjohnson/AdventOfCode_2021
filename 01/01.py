import sys

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

	
#print(measurements)
increases = [i+1 for i in range(len(measurements) - 1) if measurements[i+1] > measurements[i] ]

print(increases)
print(len(increases))
	
exit(0)

