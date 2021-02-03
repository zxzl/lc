"""
competitve means leftmost number is smaller
so we need to choose smallest number first 
(this number should at least k-1 number at right. )
-> TLE ㅠ

append to stack..pop if top of stack is smaller and k-1 number left
"""

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        
        for (i, n) in enumerate(nums):
            if len(ans) == 0:
                ans.append(n)
                continue
            
            more = len(nums) - i
            while len(ans) > 0 and ans[-1] > n and more >= k - (len(ans) - 1):
                ans.pop()
            if len(ans) < k:
                ans.append(n)
            
        return ans
                
                
            
            
