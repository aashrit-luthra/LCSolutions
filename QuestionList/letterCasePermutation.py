class Solution:
    def letterRecursive(self, s, idx, strings):
        if idx >= len(s):
            strings.add(s)
            return
        self.letterRecursive(s, idx+1, strings)
        if s[idx].isalpha():
            currLetter = s[idx].upper() if 'a' <= s[idx] <= 'z' else s[idx].lower()
            self.letterRecursive(s[:idx]+currLetter+s[idx+1:], idx+1, strings)
    
    def letterCasePermutation(self, s: str) -> List[str]:
        strings = set()
        self.letterRecursive(s, 0, strings)
        return list(strings)