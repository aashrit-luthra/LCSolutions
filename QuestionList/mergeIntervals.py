class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        if not intervals:
            return intervals
        startTime = intervals[0][0]
        endTime = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= endTime:
                endTime = max(endTime, intervals[i][1])
            else:
                output.append([startTime, endTime])
                startTime = intervals[i][0]
                endTime = intervals[i][1]
        output.append([startTime, endTime])
        return output