# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N = int(input())
roads = input()

dp = [0] * (N+5)
dp[0] = 1

for i in range(N):
	i = int(i)
	if i - 1 >= 0 and roads[i-1] == "1":
		dp[i] += dp[i-1]
	if i -2 >= 0 and roads[i-2] == "1":
		dp[i] += dp[i-2]

#print(dp)
print(dp[N-1])
