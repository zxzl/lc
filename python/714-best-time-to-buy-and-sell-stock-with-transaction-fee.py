"""
there are two states
holding - not holding

h -3 -3 -3 -3 -1 -1
e  0  0  0  5  5  8

"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        
        holding = [0] * (N+1)
        empty = [0] * (N+1)
        
        holding[0] = -1 * (prices[0] + fee)
        empty[0] = 0
        
        for i in range(1, N):
            #1. holding -> buy new or keep already bought one
            holding[i] = max(
                holding[i-1],
                empty[i-1] - prices[i] - fee
            )
            
            #2. empty -> do nothing or sell
            empty[i] = max(
                empty[i-1],
                holding[i-1] + prices[i]
            )
            
        return max(holding[N-1], empty[N-1])
