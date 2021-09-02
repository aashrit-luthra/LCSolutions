class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            currNum = abs(nums[i])
            if nums[currNum-1] < 0:
                output.append(currNum)
            else:
                nums[currNum-1] = -nums[currNum-1]
        return output