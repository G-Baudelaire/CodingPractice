from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 2:
            return 0

        intervals.sort(key=lambda interval: interval[0])

        previous, current, removals = 0, 1, 0
        while current < n:
            if intervals[previous][1] <= intervals[current][0]:
                previous += 1
                current += 1
            elif intervals[current][1] <= intervals[previous][1]:
                previous = current
                current += 1
                removals += 1
            else:
                current += 1
                removals += 1

        return removals
