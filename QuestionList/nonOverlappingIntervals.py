class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return []
        numRemovals = 0
        intervals.sort(key=lambda x: x[0])
        runningInterval = intervals[0]
        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            if currInterval[0] >= runningInterval[1]:
                runningInterval = currInterval
            else:
                runningInterval[1] = min(runningInterval[1], currInterval[1])
                numRemovals += 1
        return numRemovals