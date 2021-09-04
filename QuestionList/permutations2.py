from collections import Counter
class Solution:
    def permuteUniqueRecursive(self, arrSoFar, idx, nums, permutations, count):
        if len(arrSoFar) == len(nums):
            permutations.append(arrSoFar.copy())
            return
        
        for i in count:
            if count[i] > 0:
                count[i] -= 1
                arrSoFar.append(i)
                self.permuteUniqueRecursive(arrSoFar, i+1, nums, permutations, count)
                count[i] += 1
                arrSoFar.pop()
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        count = Counter(nums)
        self.permuteUniqueRecursive([], 0, nums, permutations, count)
        return permutations