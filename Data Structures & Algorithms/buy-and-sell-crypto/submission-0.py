class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0
        for idx, val in enumerate(prices):
            min_price = min(min_price, val)
            res = max(res, val-min_price)
        return res

        