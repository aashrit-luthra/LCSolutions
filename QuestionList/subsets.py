class Solution:
    def subsetsRecursive(self, arr, nums, idx, subsets):
        if idx == len(nums):
            subsets.append(arr)
            return
        self.subsetsRecursive(arr, nums, idx+1, subsets)
        self.subsetsRecursive(arr+[nums[idx]], nums, idx+1, subsets)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.subsetsRecursive([],nums,0,subsets)
        return subsets