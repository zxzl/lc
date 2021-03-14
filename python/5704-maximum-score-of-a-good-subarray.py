"""
O(N) solution



"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        max_score = 0
        l = k
        r = k
        m = nums[k]
        
        while True:
            
            max_score = max(max_score, m * (r-l+1))
            
            if l-1 >=0 and r+1 < N:
                # we'd better expand to larger one
                if nums[l-1] > nums[r+1]:
                    l -= 1
                    m = min(nums[l], m)
                else:
                    r += 1
                    m = min(nums[r], m)
            elif l-1 >= 0:
                l -= 1
                m = min(nums[l], m)
            elif r+1 < N:
                r += 1
                m = min(nums[r], m)
            else:
                break
                
        return max_score
            
            
            
