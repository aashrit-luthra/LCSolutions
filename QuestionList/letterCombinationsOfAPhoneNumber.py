class Solution:
    def letterCombRecursive(self, stringSoFar, idx, digits, combinations, numberMapping):
        if idx == len(digits):
            combinations.append("".join(stringSoFar))
            return
        for c in numberMapping[int(digits[idx])]:
            stringSoFar.append(c)
            self.letterCombRecursive(stringSoFar, idx+1, digits, combinations, numberMapping)
            stringSoFar.pop()
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        numberMapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        combinations = []
        self.letterCombRecursive([], 0, digits, combinations, numberMapping)
        return combinations