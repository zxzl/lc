"""
buy-sell&cooldown + subproblem
"""

from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        @lru_cache(None)
        def dp(start):
            if start >= N:
                return 0
            
            max_profit = 0
            
            # skip today
            max_profit = max(max_profit, dp(start+1))
            
            # buy today
            buy_price = prices[start]
            for sell_index in range(start+1, N):
                sell_price = prices[sell_index]
                profit = sell_price - buy_price
                rest_profit = dp(sell_index + 2)
                
                max_profit = max(max_profit, profit + rest_profit)
            
            return max_profit
        
        return dp(0)
            
