import numpy as np
from sys import argv

def load_board(lines):
	arr = []
	for i in range(5):
		line = [int(i) for i in lines.pop(0).split()]
		arr.append(line)
	if lines and len(lines) > 0:
		lines.pop(0)
	return arr, lines

def check_board(board):
	for row in board:
		if all([col == None for col in row]):
			return True
	for icol in range(len(board)):
		if all([row[icol] == None for row in board]):
			return True
	return False

def read_num(num, boards):
	for board in boards:
		for row in board:
			for icol, col in enumerate(row):
				if col == num:
					row[icol] = None
	return boards

def compute_score(board, last_num):
	print(board)
	s = 0
	for row in board:
		s = s + sum([c for c in row if c != None])
	result = s * num
	print(f"Product of remaining elements: {result}")
		

if len(argv) != 2:
	print(f"Usage: {argv[0]} <filename>")
	exit(1)

fin = open(argv[1], "r")
lines = fin.readlines()

nums = lines.pop(0).split(",")
lines.pop(0)

boards = []
while len(lines) > 1:
	board, lines = load_board(lines)
	boards.append(board)

while len(nums) > 0:
	num = int(nums.pop(0))
	boards = read_num(num, boards)
	found_boards = []
	for board in boards:
		if check_board(board):
			found_boards.append(board)
	if len(found_boards) > 0:
		if len(boards) > 1:
			for board in found_boards:
				boards.remove(board)
		elif len(boards) == 1:
			compute_score(found_boards[0], num)
			exit(0)

print("No found result.")
print(boards)
exit(1)
