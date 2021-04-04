import math


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:

        ans = 0

        nums = set(nums)
        MAX = max(nums)

        # for all possible gcd
        for i in range(1, MAX + 1):
            g = None
            for j in range(i, MAX + 1, i):
                if j not in nums:
                    continue

                if g is None:
                    g = j
                else:
                    g = math.gcd(g, j)

                if g == i:
                    ans += 1
                    break

        return ans
