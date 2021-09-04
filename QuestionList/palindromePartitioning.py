class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def partitionRecursive(self, arrSoFar, idx, s, partitions):
        if idx == len(s):
            partitions.append(arrSoFar.copy())
            return
        
        for i in range(idx, len(s)):
            newString = s[idx:i+1]
            if self.isPalindrome(newString):
                arrSoFar.append(newString)
                self.partitionRecursive(arrSoFar, i+1, s, partitions)
                arrSoFar.pop()
            
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        self.partitionRecursive([], 0, s, partitions)
        return partitions