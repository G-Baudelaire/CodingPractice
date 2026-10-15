import bisect
from typing import List


class Solution:
    def insert(self, ordered_interval: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        ordered = self._insert_interval_by_start(ordered_interval, new_interval)
        return self._merge_ordered_intervals(ordered)

    def _insert_interval_by_start(self, intervals, new_interval):
        starts = [s for s, _ in intervals]
        insert_index = bisect.bisect(starts, new_interval[0])
        return intervals[:insert_index] + [new_interval] + intervals[insert_index:]

    def _merge_ordered_intervals(self, intervals):
        merged_list = []
        for interval in intervals:
            if not merged_list or merged_list[-1][1] < interval[0]:
                merged_list.append(interval)
            else:
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])
            print(merged_list)
        return merged_list
