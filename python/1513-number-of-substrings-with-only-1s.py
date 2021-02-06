"""
for each series of 1s with size n,

there are n(n+1)/2 substring with only 1

"""

MOD = 10**9 + 7

class Solution:
    def numSub(self, s: str) -> int:
        
        answer = 0
        
        continuous = 0
        
        for c in s:
            if c == "0":
                answer += (continuous * (continuous+1) / 2) % MOD
                continuous = 0        
            if c == "1":
                continuous += 1
        
        answer += (continuous * (continuous+1) / 2) % MOD
        
        return int(answer) % MOD
        
