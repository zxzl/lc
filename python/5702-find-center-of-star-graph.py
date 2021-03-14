from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        a = defaultdict(int)
        
        for (i, j) in edges[:2]:
            a[i] += 1
            a[j] += 1
            
        soretd_pairs = sorted(a.items(), key=lambda p: p[1], reverse=True)
        
        return soretd_pairs[0][0]
