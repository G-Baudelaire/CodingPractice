from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid = tuple(tuple(row) for row in grid)
        row_dictionary = defaultdict(int)
        column_dictionary = defaultdict(int)

        for row in grid:
            row_dictionary[row] += 1

        for i in range(len(grid[0])):
            column = tuple(row[i] for row in grid)
            column_dictionary[column] += 1

        pairs = 0
        for key, value in row_dictionary.items():
            if key in column_dictionary:
                pairs += value * column_dictionary[key]
        return pairs