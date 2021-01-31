class Solution:
    def expand(self, s):
        return sorted(self._expand(s))
    def _expand(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        
        if s[0] == "{":
            i = 1
            while s[i] != "}":
                i += 1
            chars = s[1:i].split(",")
            rest = self.expand(s[i+1:])

            ans = []
            for c in chars:
                for r in rest:
                    ans.append(c+r)
            return ans
                    
        rest = self.expand(s[1:])
        return [ s[0] + r for r in rest]
    
        
