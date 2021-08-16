class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            curr = abs(nums[i])
            nums[curr - 1] = -abs(nums[curr-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        return output