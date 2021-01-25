"""
naive: 2**n (for each combination, append each element if there's no overlap with previous elements)
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        s = [set(a) for a in arr if len(set(a)) == len(a)]
        
        ans = self.helper(s, set())
        
        return len(ans)
        
        
    def helper(self, s, prev):
        if len(s) == 0:
            return prev
        
        common = s[0] & prev
        if len(common) > 0:
            return self.helper(s[1:], prev)
        
        with_s0 = self.helper(s[1:], s[0] | prev)
        without_s0 = self.helper(s[1:], prev)
        
        if len(with_s0) >= len(without_s0):
            return with_s0
        return without_s0
        
        
        
        
