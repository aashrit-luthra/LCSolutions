class Solution:        
    def combinationSumRecursive(self, arrSoFar, sumSoFar, target, candidates, combinations, idx):
        if sumSoFar == target:
            combinations.append(arrSoFar.copy())
            return
        if sumSoFar > target:
            return
        
        for i in range(idx, len(candidates)):
            arrSoFar.append(candidates[i])
            self.combinationSumRecursive(arrSoFar, sumSoFar + candidates[i], target, candidates, combinations, i)
            arrSoFar.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.combinationSumRecursive([], 0, target, candidates, combinations, 0)
        return combinations