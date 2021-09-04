class Solution:
    def generatePRecursive(self, stringSoFar, numOpening, numClosing, n, combinations):
        if (numOpening == numClosing) and (numOpening == n):
            combinations.append("".join(stringSoFar))
            return
        
        if numOpening == numClosing:
            self.generatePRecursive(stringSoFar + ["("], numOpening + 1, numClosing, n, combinations)
        elif (numOpening == n) and (numClosing < n):
            self.generatePRecursive(stringSoFar + [")"], numOpening, numClosing + 1, n, combinations)
        else:
            self.generatePRecursive(stringSoFar + ["("], numOpening + 1, numClosing, n, combinations)
            self.generatePRecursive(stringSoFar + [")"], numOpening, numClosing + 1, n, combinations)
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        self.generatePRecursive([], 0, 0, n, combinations)
        return combinations