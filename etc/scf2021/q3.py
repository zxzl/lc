# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import defaultdict

N= int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
	line = input()
	for c in range(N):
		board[r][c] = line[c]

ans = defaultdict(int)

size = 1

while size <= N:

	for r in range(N):
		for c in range(N):
			can_fill = True
			for rr in range(size):
				for cc in range(size):
					if r + rr >= N or c + cc >= N or board[r + rr][c + cc] != "1":
						can_fill = False
						break
				if not can_fill:
					break
			if can_fill:
				ans[size] += 1

	if ans[size] == 0:
		break
	size += 1

total = sum(ans.values())
print(f"total: {total}")

for (k, v) in ans.items():
	if v == 0:
		continue
	print(f"size[{k}]: {v}")
