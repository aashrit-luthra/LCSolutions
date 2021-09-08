class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        startIdx, endIdx = 0, 0
        sumSoFar = 0
        minSubarrayLength = float('inf')
        while endIdx < len(nums):
            while endIdx < len(nums) and sumSoFar < target:
                sumSoFar += nums[endIdx]
                endIdx += 1
            while endIdx <= len(nums) and sumSoFar >= target:
                minSubarrayLength = min(minSubarrayLength, endIdx - startIdx)
                sumSoFar -= nums[startIdx]
                startIdx += 1
            
        if minSubarrayLength == float('inf'):
            minSubarrayLength = 0
        return minSubarrayLength