class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        appended = False
        mergedIntervals = []
        for i in range(len(intervals)):
            currInterval = intervals[i]
            if currInterval[0] > newInterval[1]:
                if not appended:
                    appended = True
                    mergedIntervals.append(newInterval)
                mergedIntervals.append(currInterval)
            elif currInterval[1] < newInterval[0]:
                mergedIntervals.append(currInterval)
            else:
                newInterval[0] = min(newInterval[0], currInterval[0])
                newInterval[1] = max(newInterval[1], currInterval[1])
        if not appended:
            mergedIntervals.append(newInterval)
        return mergedIntervals