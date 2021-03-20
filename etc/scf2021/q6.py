# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
C, R = input().split()
C = int(C)
R = int(R)

boards = [[0 for _ in range(C)]]
for r in range(R):
	boards.append(
		[int(c) for c in input().split()]
	)

for r in range(1, R+1):
	for c in range(C):
		upper = boards[r-1][c]
		left = boards[r][c-1] if c -1 >= 0 else 0

		boards[r][c] += max(upper, left)


#print(boards)
print(boards[R][C-1])
