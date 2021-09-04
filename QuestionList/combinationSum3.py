class Solution:
    def combinationSum3Recursive(self, arrSoFar, sumSoFar, k, n, idx, nums, combinations):
        if sumSoFar == n and len(arrSoFar) == k:
            combinations.append(arrSoFar.copy())
            return
        if sumSoFar > n:
            return
        for i in range(idx, len(nums)):
            arrSoFar.append(nums[i])
            self.combinationSum3Recursive(arrSoFar, sumSoFar + nums[i], k, n, i + 1, nums, combinations)
            arrSoFar.pop()
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        nums = [1,2,3,4,5,6,7,8,9]
        self.combinationSum3Recursive([], 0, k, n, 0, nums, combinations)
        return combinations