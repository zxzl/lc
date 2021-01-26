class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        ans = self.helper(S, [""])

        return ans


    def helper(self, s, previous):
        if len(s) == 0:
            return previous

        if s[0] in "0123456789":
            new_prev =  [p + s[0] for p in previous]
            return self.helper(s[1:], new_prev)

        new_prev = [p + s[0].lower() for p in previous] + [p + s[0].upper() for p in previous]
        return self.helper(s[1:], new_prev)

