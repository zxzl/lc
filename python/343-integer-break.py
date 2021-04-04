class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        if n % 3 == 0:
            return pow(3, n // 3)
        if n % 3 == 1:
            return pow(3, (n-4) //3)*4

        return pow(3, (n-2) // 3) * 2
