"""
* if we change 0 -> 1, we have to change 1 -> 0 another place
* count the number of 0 in range and it will be number of swaps required
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        N = len(data)
        total = sum(data)
        
        # [0, total)
        num_ones = sum(data[:total])
        ans = total - num_ones
        
        # scan for [1, total+1)  ~ [N-total, N)
        for end in range(total, N):
            start = end-total + 1
            
                        
            # update num_ones
            if data[start - 1] == 1:
                num_ones -= 1
            
            if data[end] == 1:
                num_ones += 1
            #print(N, total, num_ones, start, end)
                
            ans = min(ans, total - num_ones)
        
        return ans
            
            
            
            
