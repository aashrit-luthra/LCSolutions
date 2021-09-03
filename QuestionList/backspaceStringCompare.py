class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sPointer = len(s)-1
        tPointer = len(t)-1
        tBacks = 0
        sBacks = 0
        while sPointer >= 0 or tPointer >= 0:
            while sPointer >= 0:
                if s[sPointer] == "#":
                    sBacks += 1
                    sPointer -= 1
                elif sBacks > 0:
                    sPointer -= 1
                    sBacks -= 1
                else:
                    break
            while tPointer >= 0:
                if t[tPointer] == "#":
                    tBacks += 1
                    tPointer -= 1
                elif tBacks > 0:
                    tPointer -= 1
                    tBacks -= 1
                else:
                    break
            
            if sPointer >= 0 and tPointer >= 0 and s[sPointer] != t[tPointer]:
                return False
            
            if (sPointer >= 0) != (tPointer >= 0):
                return False
        
            sPointer -= 1
            tPointer -= 1
        return True