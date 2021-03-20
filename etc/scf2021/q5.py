# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import heapq

C, R = input().split()
R = int(R)
C = int(C)

boards = []
for _ in range(R):
	l = input()
	boards.append([c for c in l])

moves = [[float('inf') for _ in range(C)]
				for _ in range(R)]

q = []
for c in range(C):
	if boards[0][c] == "c":
		moves[0][c] = 0
		q.append((0, 0, c))

while q:
	(d, r, c) = heapq.heappop(q)

	if moves[r][c] < d:
		continue

	for (nr, nc) in [(r, c+1), (r, c-1), (r+1, c)]:
		if not(0 <= nr < R and 0 <= nc < C):
			continue
		if boards[nr][nc] == "x":
			continue
		nd = d
		if nr == r:
			nd += 1

		if nd < moves[nr][nc]:
			heapq.heappush(q, (nd, nr, nc))
			moves[nr][nc] = nd

ans = min(moves[R-1])
if ans == float('inf'):
	print(-1)
else:
	print(ans)
