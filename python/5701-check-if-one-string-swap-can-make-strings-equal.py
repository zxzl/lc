class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        d1 = None
        d2 = None
        
        N = len(s1)
        for i in range(N):
            if s1[i] == s2[i]:
                continue
            
            if not d1:
                d1 = (s1[i], s2[i])
            elif not d2:
                d2 = (s1[i], s2[i])
            else:
                return False
            
        if not d1 and not d2:
            return True
        
        if not d2:
            return False
        
        return d1[0] == d2[1] and d1[1] == d2[0]
