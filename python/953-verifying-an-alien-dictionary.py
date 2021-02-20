class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        c_order = {}
        for (i, c) in enumerate(order):
            c_order[c] = i
            
        def isSmallOrEqual(a, b):
            A = len(a)
            B = len(b)
            C = min(A, B)
            
            for i in range(C):
                if c_order[a[i]] < c_order[b[i]]:
                    return True
                elif c_order[a[i]] > c_order[b[i]]:
                    return False
                
            # a[:C] and b[:C] is same
            return A <= B
        
        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            
            if not isSmallOrEqual(a, b):
                return False
        
        return True
