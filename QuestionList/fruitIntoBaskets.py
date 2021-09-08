class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        startIdx, endIdx = 0, 0
        maxFruits = 0
        fruitMapping = {}
        while endIdx < len(fruits):
            while endIdx < len(fruits) and len(fruitMapping) <= 2:
                print(startIdx, endIdx)
                if not fruits[endIdx] in fruitMapping:
                    fruitMapping[fruits[endIdx]] = 0
                fruitMapping[fruits[endIdx]] += 1
                if len(fruitMapping) <= 2:
                    maxFruits = max(maxFruits, endIdx - startIdx + 1)
                endIdx += 1
            while endIdx < len(fruits) and len(fruitMapping) > 2:
                fruitMapping[fruits[startIdx]] -= 1
                if not fruitMapping[fruits[startIdx]]:
                    del fruitMapping[fruits[startIdx]]
                startIdx += 1
                
        return maxFruits