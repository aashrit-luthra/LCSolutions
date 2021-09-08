class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        mergedIntervals = []
        intervals.sort(key=lambda x: x[0])
        runningInterval = intervals[0]
        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            if currInterval[0] > runningInterval[1]:
                # merge
                mergedIntervals.append(runningInterval)
                runningInterval = currInterval
            else:
                # keep updating
                runningInterval[1] = max(runningInterval[1], currInterval[1])
        mergedIntervals.append(runningInterval)
        return mergedIntervals