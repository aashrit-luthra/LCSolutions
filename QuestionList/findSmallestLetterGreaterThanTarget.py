class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] > target and (mid == 0 or letters[mid-1] <= target):
                return letters[mid]
            elif letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[0]