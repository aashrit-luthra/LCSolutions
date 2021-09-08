class Solution:
    def reverseWords(self, s: str) -> str:
        newS = s.split()
        i = 0
        j = len(newS)-1
        while i <= j:
            newS[i], newS[j] = newS[j], newS[i]
            i += 1
            j -= 1
        newS = " ".join(newS)
        return newS