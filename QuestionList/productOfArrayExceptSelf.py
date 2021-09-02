class Solution:
    def getPrefixArr(self, nums):
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1]
    
    def getSuffixArr(self, nums):
        output = [1 for i in range(len(nums))]
        cumProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            cumProduct *= nums[i]
            output[i] = cumProduct
        return output
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixArr = self.getSuffixArr(nums)
        self.getPrefixArr(nums)
        for i in range(len(nums)):
            leftSide = 1
            if i > 0:
                leftSide = nums[i-1]
            rightSide = 1
            if i < len(nums) - 1:
                rightSide = suffixArr[i+1]
            suffixArr[i] = leftSide * rightSide
        return suffixArr