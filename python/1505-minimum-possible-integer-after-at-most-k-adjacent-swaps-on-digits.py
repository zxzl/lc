from collections import defaultdict, deque
import bisect

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        arr = list(num)
        
        ans = self.sol(arr, k)
        
        
        return ans
        
    def sol(self, arr, k):
        h = defaultdict(deque)
        
        for (i, v) in enumerate(arr):
            h[v].append(i)
            
        inserted_i = []
        ans = ""
        for _ in range(len(arr)):
            for d in "0123456789":
                if len(h[d]) == 0:
                    continue
                
                old_p = h[d][0]
                #new_p = index for array with elements not moved yet

                num_smaller = bisect.bisect_left(inserted_i, old_p)
                new_p = old_p - num_smaller
                
                if new_p <= k:
                    k -= new_p
                    ans += d
                    bisect.insort(inserted_i, old_p)
                    h[d].popleft()
                    break
            
        return ans
