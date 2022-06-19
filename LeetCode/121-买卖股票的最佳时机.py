"""
Dynamic programming: max profit at day i = max(
    max profit at day i - 1, price at day i - minimum price before day i
    )
"""
class Solution:
    def maxProfit(self, prices):
        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return dp[-1]
