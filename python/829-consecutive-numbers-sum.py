"""
even: cannot

if we represent each number as a + i(1~)

sum = P*a + P(P+1)/2

9
P=2
a=3
4,5

P=3
a=1
2,3,4
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        sol = 0
        
        p = 1
        
        while True:
            rest = N - p*(p+1)/2
            if rest < 0:
                break
                
            if rest % p == 0:
                sol += 1
            
            p += 1
            
        return sol
        
