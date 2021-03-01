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

# class Solution:
#     def minInteger(self, num: str, k: int) -> str:
#         arr = list(num)
        
#         ans = self.sol(arr, k)
        
        
#         return "".join(ans)
        
#     def sol(self, arr, k):
#         if k <= 0:
#             return arr
        
#         if len(arr) == 0:
#             return []
        
#         min_i = 0
#         min_v = arr[0]
        
#         for i in range(1, min(k+1, len(arr))):
#             if min_v == "0":
#                 break
#             if arr[i] < min_v:
#                 min_i = i
#                 min_v = arr[i]

        
#         remaining_k = k - min_i
#         arr.pop(min_i)
        
#         return [min_v] + self.sol(arr, remaining_k)
