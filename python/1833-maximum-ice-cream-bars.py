class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        balance = coins

        n = 0

        for c in costs:
            if balance >= c:
                n += 1
                balance -= c
            else:
                break

        return n
