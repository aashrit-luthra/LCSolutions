class Solution:
    def findTargetRecursive(self, nums, idx, sumSoFar, target, memo):
        if idx == len(nums):
            if sumSoFar == target:
                return 1
            else:
                return 0
            
        if (idx, sumSoFar) not in memo:
            memo[(idx, sumSoFar)] = self.findTargetRecursive(nums, idx + 1, sumSoFar + nums[idx], target, memo) + self.findTargetRecursive(nums, idx+1, sumSoFar - nums[idx], target, memo)
        
        return memo[(idx, sumSoFar)]
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.findTargetRecursive(nums, 0, 0, target, memo)