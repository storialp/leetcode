class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Use pointers to go through all windows and check which one maximizes
        # profit
        l, r = 0, 1 
        # Deals with case where no profit can be made
        max_profit = 0
        while r < len(prices):
            # first check if profitable
            window_profit = prices[r] - prices[l] 
            if window_profit > 0:
                max_profit = max(window_profit, max_profit) 
            else:
                l = r
            r += 1
        return max_profit