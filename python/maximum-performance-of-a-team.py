"""
sort engineers by efficiency..?

[2,10,3,1,5,8]
[5,4,3,9,7,2]

p 18 21 15  8
s  8  3 10  2 5 3
e  2  3  4  5 7 9

then problem becomes choose efficiency, and choose k-1 engineers

---

should've think of iterating form efficient workers ㅜㅜ
"""

import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        

        ans = 0
        
        speeds = []
        speedSum = 0
        for (e,s) in sorted(zip(efficiency, speed), reverse=True):
            speedSum += s
            heapq.heappush(speeds, s)
            if len(speeds) > k:
                speedSum -= heapq.heappop(speeds)
            
            ans = max(ans, e * speedSum)
            
        return ans % (10**9 + 7)
            
            
            
            
            
        
        
