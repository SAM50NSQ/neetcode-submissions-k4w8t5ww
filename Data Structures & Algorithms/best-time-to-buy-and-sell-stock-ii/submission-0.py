class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        stock = 0
        cost = 0
        profit = 0
        for i, p in enumerate(prices):
            if i < (len(prices) - 1) and p < prices[i + 1] and stock == 0:
                stock = 1
                cost = p
            elif i < (len(prices) - 1) and p > prices[i + 1] and stock == 1:
                stock = 0
                profit += p - cost
                cost = 0
            elif i == len(prices) - 1 and stock == 1:
                stock = 0
                profit += p - cost
                cost = 0
        return profit