from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 0
        points.sort(key=lambda x: x[0])
        end = float("-inf")

        for point in points:
            if end < point[0]:
                start, end = point
                arrows += 1
            else:
                end = min(end, point[1])
        return arrows
