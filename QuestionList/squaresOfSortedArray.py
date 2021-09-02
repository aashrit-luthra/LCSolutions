class Solution:
    def inBounds(self, idx, n):
        return idx >= 0 and idx < n
    
    def findPosIdx(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= 0 and (mid == 0 or nums[mid-1] < 0):
                return mid
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        return len(nums)
        
    def sortedSquares(self, nums: List[int]) -> List[int]:
        posIdx = self.findPosIdx(nums)
        negIdx = posIdx - 1
        output = []
        while self.inBounds(posIdx, len(nums)) or self.inBounds(negIdx, len(nums)):
            if self.inBounds(posIdx, len(nums)) and self.inBounds(negIdx, len(nums)):
                if abs(nums[posIdx]) >= abs(nums[negIdx]):
                    output.append(nums[negIdx]**2)
                    negIdx -= 1
                else:
                    output.append(nums[posIdx]**2)
                    posIdx += 1
            elif self.inBounds(posIdx, len(nums)):
                output.append(nums[posIdx]**2)
                posIdx += 1
            else:
                output.append(nums[negIdx]**2)
                negIdx -= 1
        return output