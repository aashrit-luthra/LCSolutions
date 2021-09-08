class Solution:    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersectedIntervals = []
        firstPointer = 0
        secondPointer = 0
        while firstPointer < len(firstList) and secondPointer < len(secondList):
            firstInterval = firstList[firstPointer]
            secondInterval = secondList[secondPointer]
            if (secondInterval[0] >= firstInterval[0] and secondInterval[0] <= firstInterval[1]) or (firstInterval[0] >= secondInterval[0] and firstInterval[0] <= secondInterval[1]):
                start = max(firstInterval[0], secondInterval[0])
                end = min(firstInterval[1], secondInterval[1])
                intersectedIntervals.append([start,end])

            if firstInterval[1] < secondInterval[1]:
                firstPointer += 1
            elif secondInterval[1] < firstInterval[1]:
                secondPointer += 1
            else:
                firstPointer += 1
                secondPointer += 1
        
        return intersectedIntervals