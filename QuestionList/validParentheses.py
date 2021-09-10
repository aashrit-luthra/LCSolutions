class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(":")", "{":"}", "[":"]"}
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack or brackets[stack[-1]] != c:
                    return False
                stack.pop()
        return len(stack) == 0