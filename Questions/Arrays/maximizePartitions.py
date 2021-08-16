def getLastArray(text):
    output = [-1 for i in range(26)]
    for i in range(len(text)):
        output[ord(text[i]) - ord('a')] = i
    return output

def maximizePartitions(text):
    lastArray = getLastArray(text)
    start = right = 0
    result = []
    for i in range(len(text)):
        char = text[i]
        right = max(right, lastArray[ord(char) - ord('a')])
        if right == i:
            result.append(right-start+1)
            left = right + 1
    return result



    