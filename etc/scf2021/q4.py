# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
prefs_input = input()

prefs = {}

prefs_str = prefs_input.split()
for (i, c) in enumerate("ABCDE"):
	prefs[c] = prefs_str[i]

R, C = input().split()
R = int(R)
C = int(C)

status = [["" for _ in range(C)] for _ in range(R)]
genre = [["" for _ in range(C)] for _ in range(R)]

for r in range(R):
	l = input()
	for c in range(C):
		status[r][c] = l[c]

for r in range(R):
	l = input()
	for c in range(C):
		genre[r][c] = l[c]

contents = []

for r in range(R):
	for c in range(C):
		s = status[r][c]
		g = genre[r][c]

		if s == "W":
			continue

		seen_key = 0 if s == "Y" else 1
		genre_key = 5 - float(prefs[g])

		contents.append((seen_key, genre_key, r, c, g))

contents.sort()
for (seen_key, genre_key,r,c, g) in contents:
	print(f"{g} {prefs[g]} {r} {c}")
