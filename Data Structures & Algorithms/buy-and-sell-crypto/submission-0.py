class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, n = 0, 0, len(prices)

        best = 0
        
        while r < n:
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            best = max(best, profit)
            r += 1
        return best
