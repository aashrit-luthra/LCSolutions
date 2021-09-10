class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        idx = 0
        currentString = ""
        while idx < len(s):
            if s[idx].isalpha():
                currentString = currentString + s[idx]
                idx += 1
            elif s[idx].isnumeric():
                count = 0
                while s[idx].isnumeric():
                    count = count * 10 + int(s[idx])
                    idx += 1
                countStack.append(count)
            elif s[idx] == "[":
                stringStack.append(currentString)
                currentString = ""
                idx += 1
            elif s[idx] == "]":
                totalString = list(stringStack[-1])
                stringStack.pop()
                count = countStack[-1]
                countStack.pop()
                for i in range(count):
                    totalString.append(currentString)
                currentString = "".join(totalString)
                idx += 1
        return currentString

# Option 2
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx = 0
        s = "1[" + s + "]"
        while idx < len(s):
            if s[idx].isalpha():
                stack.append(s[idx])
                idx += 1
            elif s[idx].isnumeric():
                count = 0
                while s[idx].isnumeric():
                    count = count * 10 + int(s[idx])
                    idx += 1
                stack.append(count)
            elif s[idx] == "[":
                stack.append(s[idx])
                idx += 1
            elif s[idx] == "]":
                recentString = ""
                while stack[-1] != "[":
                    recentString = stack.pop() + recentString
                stack.pop()
                count = stack.pop()
                newString = []
                for i in range(count):
                    newString.append(recentString)
                stack.append("".join(newString))
                idx += 1
        return stack[0]