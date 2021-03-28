class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        nums = set()

        curr = ""
        for c in word:
            if c not in "0123456789":
                if len(curr) > 0:
                    nums.add(int(curr))
                curr = ""
            else:
                curr += c
        if len(curr) > 0:
            nums.add(int(curr))

        return len(nums)
