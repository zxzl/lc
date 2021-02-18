"""
kind of greedy..
1) x -> 0 : keep
2) 0 -> x : reverse
y is x's neighbor
3) y -> x : keep
4) x -> y: reverse
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        #adj = [[0 for _ in range(n)] for _ in range(n)] -> TLE
        
        adj = defaultdict(list)
        adjr = defaultdict(list)
        for (start, end) in connections:
            adj[start].append(end)
            adjr[end].append(start)
            
        self.flip = 0
        seen = set()
        def dfs(root):
            seen.add(root)
            # root -> node
            for nei in adj[root]:
                if nei in seen:
                    continue
                self.flip += 1
                dfs(nei)
            
            # node -> root
            for nei in adjr[root]:
                if nei in seen:
                    continue
                dfs(nei)
                    
        dfs(0)
        return self.flip
                    
                
                
            
        
            
            
