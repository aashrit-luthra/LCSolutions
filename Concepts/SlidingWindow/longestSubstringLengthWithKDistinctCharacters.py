def longestSubstringLengthWithKDistinctCharacters(string, k):
    characters = {}
    j = 0
    count = 0
    maxLength = float('-inf')
    for i in range(len(string)):
        if string[i] not in characters:
            characters[string[i]] = 1
            count += 1
        else:
            characters[string[i]] += 1
        
        while count > k:
            characters[string[j]] -= 1
            if characters[string[j]] == 0:
                count -= 1
            j += 1
        if count == k:
            maxLength = max(maxLength, i - j + 1)
    return maxLength

print(longestSubstringLengthWithKDistinctCharacters("aaahhibc", 2))


    
 

