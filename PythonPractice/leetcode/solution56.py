from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = self._sort_intervals_by_start(intervals)
        merged_intervals = []
        for interval in sorted_intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        return merged_intervals

    def _sort_intervals_by_start(self, intervals: List[List[int]]):
        return sorted(intervals, key=lambda interval: interval[0])
