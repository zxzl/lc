"""
naive(ㅜㅜ): O(N^2)
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []


        for (i, num) in enumerate(nums):
            curr = (i + 1) % N

            found = False
            while not found and curr != i:
                if nums[curr] > num:
                    ans.append(nums[curr])
                    found=True
                else:
                    curr = (curr+1)%N

            if not found:
                ans.append(-1)

        return ans
