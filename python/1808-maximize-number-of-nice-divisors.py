MOD = 10 ** 9 + 7

class Solution:
    def maxNiceDivisors(self, n: int) -> int:

        if n <= 3:
            return n


        if n % 3 == 0:
            return pow(3, n // 3, MOD)

        if n % 3 == 1:
            # 2 2 + rest 3
            return (pow(3, (n-4) // 3, MOD) * 4) % MOD

        # 2 rest 3
        return (pow(3, (n-2) // 3, MOD) * 2) % MOD
