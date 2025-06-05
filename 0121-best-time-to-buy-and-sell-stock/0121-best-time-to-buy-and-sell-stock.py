class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minPrice=prices[0]
        for i in prices:
            if i<minPrice:
                minPrice=i
            else:
                diff=i-minPrice
                profit=max(diff,profit)
        return profit
        