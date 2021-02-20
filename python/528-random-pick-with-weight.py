import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        
        self.cum_weights = [0]
        for i in w:
            self.cum_weights.append(self.cum_weights[-1] + i/total)
        

    def pickIndex(self) -> int:
        r = random.random()
        
        i = bisect.bisect_right(self.cum_weights, r)
        return i-1
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
