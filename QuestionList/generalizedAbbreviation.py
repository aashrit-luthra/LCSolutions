class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateARecursive(self, stringSoFar, idx, word, abbreviations):
        if idx == len(word):
            abbreviations.append("".join(stringSoFar))
            return
        
        for i in range(idx, len(word)):
            newWord = word[idx:i+1]
            if not stringSoFar:
                self.generateARecursive(stringSoFar + [newWord], i+1, word, abbreviations)
                self.generateARecursive(stringSoFar + [str(len(newWord))], i+1, word, abbreviations)
            else:
                if stringSoFar[-1].isnumeric():
                    self.generateARecursive(stringSoFar + [newWord], i+1, word, abbreviations)
                else:
                    self.generateARecursive(stringSoFar + [str(len(newWord))], i+1, word, abbreviations)

    def generateAbbreviations(self, word):
        abbreviations = []
        self.generateARecursive([], 0, word, abbreviations)
        return abbreviations