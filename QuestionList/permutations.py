class Solution:
    def permuteRecursive(self, arr, nums, permutations):
        if len(arr) == len(nums):
            permutations.append(arr.copy())
            return
        for i in range(len(nums)):
            if nums[i] in arr:
                continue
            arr.append(nums[i])
            self.permuteRecursive(arr, nums, permutations)
            arr.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permuteRecursive([],nums, permutations)
        return permutations