# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

N = int(user_input)


events = []

for i in range(N):
	l = input()
	start = l[:5]
	end = l[7:]

	events.append((start.strip(), 'START', i))
	events.append((end.strip(), 'END', i))

events.sort()

n_available = 0
overlap_start = None
overlap_end = None

for (t, e, i) in events:
	if e == "START":
		n_available += 1
		if n_available == N:
			overlap_start = t
	elif e == "END":
		n_available -= 1
		if n_available == N - 1:
			overlap_end = t

if overlap_start is not None and overlap_end is not None:
	output = overlap_start + " ~ " + overlap_end
	print(output)
else:
	print("-1")
