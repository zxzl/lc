from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        d = defaultdict(int)
        
        for t in time:
            mod = t % 60
            d[mod] += 1
            
        
        ans = 0
        
        # mod:0,30 -> they can make pair by themselves
        ans += d[0] * (d[0]-1) // 2
        ans += d[30] * (d[30]-1) // 2
        # mod (1~29) -> make pair with 60-i
        for i in range(1, 30):
            counterpart = 60-i
            ans += d[i] * d[counterpart]
            
        return ans
        
        
            
