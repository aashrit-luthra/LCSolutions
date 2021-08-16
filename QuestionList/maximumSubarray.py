class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = float('-inf')
        currentSum = 0
        for num in nums:
            currentSum = max(currentSum + num, num)
            globalMax = max(globalMax, currentSum)
        return globalMax