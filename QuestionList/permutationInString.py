class Solution:
    def lessThanOrEqualKeys(self, runningDict, originalDict):
        runningDictKeys = set(runningDict.keys())
        originalDictKeys = set(originalDict.keys())
        return len(runningDictKeys - originalDictKeys) == 0
        
    def lessThanOrEqualValues(self, runningDict, originalDict):
        for key, value in runningDict.items():
            if value > originalDict[key]:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create original dictionary
        originalDict = {}
        for c in s1:
            if c not in originalDict:
                originalDict[c] = 0
            originalDict[c] += 1
        
        runningDict = {}
        startIdx, endIdx = 0, 0
        while endIdx < len(s2):
            while endIdx < len(s2) and self.lessThanOrEqualKeys(runningDict, originalDict) and self.lessThanOrEqualValues(runningDict, originalDict):
                if runningDict == originalDict:
                    return True
                if not s2[endIdx] in runningDict:
                    runningDict[s2[endIdx]] = 0
                runningDict[s2[endIdx]] += 1
                endIdx += 1
            if runningDict == originalDict:
                return True
            while not self.lessThanOrEqualKeys(runningDict, originalDict) or not self.lessThanOrEqualValues(runningDict, originalDict):
                runningDict[s2[startIdx]] -= 1
                if not runningDict[s2[startIdx]]:
                    del runningDict[s2[startIdx]]
                startIdx += 1
        return False