class UnionFind:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.rank = [0] * n
        
    def query(self, q):
        if q != self.arr[q]:
            self.arr[q] = self.query(self.arr[q])
        return self.arr[q]
    
    def merge(self, a, b):
        pa = self.query(a)
        pb = self.query(b)
        
        if pa == pb:
            return False
        
        if self.rank[a] < self.rank[b]:
            self.arr[pa] = pb
        elif self.rank[a] > self.rank[b]:
            self.arr[pb] = pa
        else:
            self.arr[pb] = pa
            self.rank[pa] += 1
        
        return True

from collections import defaultdict    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        nums = list(set(nums))
        
        v2i = defaultdict(list)
        for (i, n) in enumerate(nums):
            v2i[n].append(i)
        
        uf = UnionFind(len(nums))
        
        for i, n in enumerate(nums):
            for j in v2i[n-1]:
                uf.merge(i, j)
            for k in v2i[n+1]:
                uf.merge(i, k)
                
        for i in range(len(nums)):
            uf.query(i)
        return max(Counter(uf.arr).values())
        
