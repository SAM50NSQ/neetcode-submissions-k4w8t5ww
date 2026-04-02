class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy + 1
        res = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            res = max(res, (prices[sell] - prices[buy]))
            sell += 1
        return res