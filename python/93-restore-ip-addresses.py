class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answers = self.recursive(s, 0)
        
        return [".".join(ans) for ans in answers]
        
    def recursive(self, s, p):
        if p == 4 and len(s) == 0:
            return [[]]
        if p == 4 and len(s) > 0:
            return []
        if len(s) == 0:
            return []
        
        ans = []
        
        # single digit
        for sol in self.recursive(s[1:], p + 1):
            ans.append( [s[0]] + sol)
            
        # no leading zero
        if s[0] == '0':
            return ans
        
        # two digit
        if len(s) >= 2:
            for sol in self.recursive(s[2:], p + 1):
                ans.append([s[:2]] + sol)
                
        if len(s) >= 3 and int(s[:3]) <= 255:
            for sol in self.recursive(s[3:], p + 1):
                ans.append([s[:3]] + sol)

        return ans
            
        
