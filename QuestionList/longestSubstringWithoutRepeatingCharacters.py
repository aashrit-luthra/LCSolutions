# while loops only
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startIdx = 0
        endIdx = 0
        charactersSeen = set()
        maxSubstring = 0
        while endIdx < len(s):
            while endIdx < len(s) and s[endIdx] not in charactersSeen:
                maxSubstring = max(maxSubstring, endIdx - startIdx + 1)
                charactersSeen.add(s[endIdx])
                endIdx += 1
            while endIdx < len(s) and s[endIdx] in charactersSeen:
                charactersSeen.remove(s[startIdx])
                startIdx += 1
        return maxSubstring

# with for loop
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startIdx = 0
        charactersSeen = set()
        maxSubstring = 0
        for endIdx in range(len(s)):
            while s[endIdx] in charactersSeen:
                charactersSeen.remove(s[startIdx])
                startIdx += 1
            maxSubstring = max(maxSubstring, endIdx - startIdx + 1)
            charactersSeen.add(s[endIdx])
        return maxSubstring