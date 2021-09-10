class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        startDay = 0
        for endDay in range(len(prices)):
            if prices[endDay] < prices[startDay]:
                startDay = endDay
            elif (endDay == 0 or prices[endDay] >= prices[endDay-1]) and (endDay == len(prices)-1 or prices[endDay] > prices[endDay+1]):
                totalProfit += prices[endDay] - prices[startDay]
                startDay = endDay
        return totalProfit