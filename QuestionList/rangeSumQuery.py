class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArray = [0 for i in range(len(nums))]
        if nums:
            self.prefixArray[0] = nums[0]
        for i in range(1, len(self.prefixArray)):
            self.prefixArray[i] = nums[i] + self.prefixArray[i-1]
            
    def sumRange(self, left: int, right: int) -> int:
        if left < 0 or left >= len(self.prefixArray) or right < 0 or right >= len(self.prefixArray):
            return -1
        rightIdxVal = self.prefixArray[right]
        leftIdxVal = self.prefixArray[left-1] if left - 1 >= 0 else 0
        return rightIdxVal - leftIdxVal
