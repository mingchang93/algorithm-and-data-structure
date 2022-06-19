class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        merged_interval = intervals[0]

        for i in range(len(intervals)):
            if intervals[i][0] <= merged_interval[1]:
                start = merged_interval[0]
                end = max(merged_interval[1], intervals[i][1])
                merged_interval = [start, end]
            else:
                res.append(merged_interval)
                merged_interval = intervals[i]

        res.append(merged_interval)

        return res