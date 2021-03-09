import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for (src, dst, w) in times:
            adj[src].append((dst, w))
        
        dist = [float('inf')] * (n+1)
        dist[0] = 0
        q = []
        
        q.append((0, k))
        dist[k] = 0
        
        while q:
            (d, node) = heapq.heappop(q)
            
            if d > dist[node]:
                continue
                
            for (dst, w) in adj[node]:
                new_d = d + w
                if new_d < dist[dst]:
                    dist[dst] = new_d
                    heapq.heappush(q, (new_d, dst))
                    
        
        t = max(dist)
        if t == float('inf'):
            return -1
        return t
                
        
