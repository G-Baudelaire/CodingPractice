from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.rows, self.columns = 0, 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows, self.columns = len(grid), len(grid[0])
        islands = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if grid[row][column] == "1":
                    islands += 1
                    self._removeIsland(grid, (row, column))
        return islands

    def _removeIsland(self, grid, starting_position):
        queue = deque([starting_position])
        while queue:
            row, column = queue.pop()
            grid[row][column] = "0"
            if column != 0 and grid[row][column - 1] == "1":
                queue.append((row, column - 1))
            if column != self.columns - 1 and grid[row][column + 1] == "1":
                queue.append((row, column + 1))
            if row != 0 and grid[row - 1][column] == "1":
                queue.append((row - 1, column))
            if row != self.rows - 1 and grid[row + 1][column] == "1":
                queue.append((row + 1, column))
