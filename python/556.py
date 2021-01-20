class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        
        nums = [int(c) for c in s]
        
        N = len(nums)
        
        st = []
        
        h = {}

        for i in range(N-1, -1, -1):
            ni = nums[i]
           
            # find number bigger
            for k in range(ni + 1, 10):
                if k in h:
                    j = h[k]
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i+1:] = sorted(nums[i+1:])
                    
                    ans = int("".join(map(str, nums)))
                    if ans > 2**31 -1 :
                        return -1
                    return ans
            h[ni] = i
            
        return -1
                
