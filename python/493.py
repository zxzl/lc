import bisect

class BIT:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n+1)
        
    def update(self, i, v):
        i += 1
        
        while i <= self.n:
            self.arr[i] += v
            i += i & -i
        
    def count(self, i):
        i += 1
        res = 0
        
        while i > 0:
            res += self.arr[i]
            i -= i & -i
        
        return res


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        N = len(nums)
        vals = sorted(list(set(nums)))
        
        v2i = {}
        for (i,v) in enumerate(vals):
            v2i[v] = i 
            
        
        bit = BIT(len(vals))
        
        ans = 0
        
        #print(vals)
        
        for (i, n) in enumerate(nums):
            max_prev = n * 2
            max_i = bisect.bisect_right(vals, max_prev) - 1
            
            cnt = i - bit.count(max_i)
            
            #print(i, n, cnt)
            ans += cnt
            
            bit.update(v2i[n], 1)
            
        return ans
