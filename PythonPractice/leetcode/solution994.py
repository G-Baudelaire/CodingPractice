from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh_oranges = {(row, column) for row in range(m) for column in range(n) if grid[row][column] == 1}
        queue = [((row, column), 0) for row in range(m) for column in range(n) if grid[row][column] == 2]
        max_distance = 0
        while queue:
            (row, column), distance = queue.pop(0)
            max_distance = max(max_distance, distance)
            adjacent = {(row - 1, column), (row, column + 1), (row - 1, column), (row, column - 1)}
            adjacent.intersection_update(fresh_oranges)
            fresh_oranges.difference_update(fresh_oranges)
            queue.extend((fresh_orange, distance + 1) for fresh_orange in fresh_oranges)

        if fresh_oranges:
            return -1
        else:
            return max_distance
