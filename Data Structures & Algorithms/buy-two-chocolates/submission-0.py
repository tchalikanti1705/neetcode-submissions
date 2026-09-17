class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = float('inf'), float('inf')
        for i in range(len(prices)):
            if prices[i] < min1:
                min2 = min1
                min1 = prices[i]
            elif prices[i] < min2:
                min2 = prices[i]
        res = money - (min1+min2)
        return res if res>=0 else money
        