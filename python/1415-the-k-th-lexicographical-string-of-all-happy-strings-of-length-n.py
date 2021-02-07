"""
n=1 -> a 1 b 1 c 1 -> 3
n=2 -> a 2 b 2 c 2 -> 6
n=3 -> a 4 b 4 c 4 -> 12
n=4 -> a 8 b 8 c 8 -> 24
n=5 -> a 16 b 16 c 16 -> 48
n=6 -> 
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if n == 1:
            if k > 3:
                return ""
            return ["a", "b", "c"][k-1]
        
        countForFirst = self.getCountForFirst(n)
        
        if k <= countForFirst:
            return "a" + self.helper(n-1, k, "a")
        
        if countForFirst < k <= 2*countForFirst:
            return "b" + self.helper(n-1, k - countForFirst, "b")
        
        if 2*countForFirst < k <= 3*countForFirst:
            return "c" + self.helper(n-1, k - countForFirst * 2, "c")
        
        return ""
    
    def helper(self, n, k, prev):
        chars = [c for c in "abc" if c != prev]
        if n == 1:
            if k > 2:
                return ""
            return chars[k-1]
            
        countForFirst = self.getCountForFirst(n)
        if k <= countForFirst:
            return chars[0] + self.helper(n-1, k, chars[0])
        if countForFirst < k <= 2*countForFirst:
            return chars[1] + self.helper(n-1, k - countForFirst, chars[1])
        
        return ""
    
    def getCountForFirst(self, n):
        return 2 ** (n-1)
