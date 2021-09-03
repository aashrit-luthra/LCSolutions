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

# Another Way
class Solution:
    def subsetsRecursive(self, arr, nums, idx, subsets):
        subsets.append(arr.copy())
        for i in range(idx, len(nums)):
            arr.append(nums[i])
            self.subsetsRecursive(arr, nums, i+1, subsets)
            arr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.subsetsRecursive([],nums,0,subsets)
        return subsets