class Solution:
    def subsetsRecursive(self, arr, nums, idx, subsets):
        subsets.append(arr.copy())
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            arr.append(nums[i])
            self.subsetsRecursive(arr, nums, i+1, subsets)
            arr.pop()
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.subsetsRecursive([], nums, 0, subsets)
        return subsets