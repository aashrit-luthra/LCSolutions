# BFS
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# DFS
from collections import deque
class Solution:
    
    def average(self, root, level, totalSumArr, totalCountArr):
        if not root:
            return
        if level >= len(totalSumArr):
            totalSumArr.append(0)
            totalCountArr.append(0)
        totalSumArr[level] += root.val
        totalCountArr[level] += 1
        self.average(root.left, level + 1, totalSumArr, totalCountArr)
        self.average(root.right, level + 1, totalSumArr, totalCountArr)
        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        totalSumArr = []
        totalCountArr = []
        output = []
        self.average(root, 0, totalSumArr, totalCountArr)
        for i in range(len(totalSumArr)):
            output.append(totalSumArr[i] / totalCountArr[i])
        return output