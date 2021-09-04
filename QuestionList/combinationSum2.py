class Solution:
    def combinationSum2Recursive(self, arrSoFar, sumSoFar, target, candidates, combinations, idx):
        if sumSoFar == target:
            combinations.append(arrSoFar.copy())
            return
        if sumSoFar > target:
            return
        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                print(i, idx, candidates)
                continue
            arrSoFar.append(candidates[i])
            self.combinationSum2Recursive(arrSoFar, sumSoFar + candidates[i], target, candidates, combinations, i + 1)
            arrSoFar.pop()
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        self.combinationSum2Recursive([], 0, target, candidates, combinations, 0)
        return combinations