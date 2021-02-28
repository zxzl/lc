"""
naive: mark an edge, and see if the graph is connected graph without the edge
"""

from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        nodes = set()
        adj = defaultdict(list)
        for (a,b) in edges:
            nodes.add(a)
            nodes.add(b)
            adj[b].append(a)
            adj[a].append(b)
        N = max(list(nodes))
    
        def can_connect_without(i_skip):
            seen = set()
            skip_edge = edges[i_skip]
            
            def dfs(r):
                if r in seen: 
                    return
                
                seen.add(r)
                for nei in adj[r]:
                    if [nei,r] == skip_edge or [r,nei] == skip_edge:
                        continue
                    if nei not in seen:
                        dfs(nei)
            dfs(1)
            return len(seen) == N
    
        for i in range(N-1, -1, -1):
            can = can_connect_without(i)
            if can:
                return edges[i]
                    
        
