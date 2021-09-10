class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        startDay = 0
        for endDay in range(len(prices)):
            if prices[endDay] > prices[startDay]:
                maxProfit = max(maxProfit, prices[endDay] - prices[startDay])
            else:
                startDay = endDay
        return maxProfit