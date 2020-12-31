class NumArray:

    def __init__(self, nums: List[int]):
        
        self.N = len(nums)
        self.arr = [0] * (self.N+1)
        self.nums = nums
        
        for (i, n) in enumerate(nums):
            self._update(i, n)
        
    def update(self, i, val):
        orig = self.nums[i]
        self.nums[i] = val
        
        diff = val - orig
        self._update(i, diff)

    def _update(self, i: int, val: int) -> None:
        i += 1
        
        while i <= self.N:
            self.arr[i] += val
            i += i & -i
        
        
    def _sum(self, i):
        i += 1
        ans = 0
        
        while i > 0:
            ans += self.arr[i]
            i -= i & -i
        
        return ans

    def sumRange(self, i: int, j: int) -> int:
        return self._sum(j) - self._sum(i-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
