from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        rows, columns = len(maze), len(maze[0])

        unvisited = set((row, column) for row in range(rows) for column in range(columns) if maze[row][column] == '.')
        queue = [(entrance, 0)]
        while queue:
            (row, column), distance = queue.pop(0)
            exit = row in {0, rows - 1} or column in {0, columns - 1}
            if (row, column) != entrance and exit:
                return distance
            adjacent = {(row - 1, column), (row, column + 1), (row - 1, column), (row, column - 1)}
            adjacent.intersection_update(unvisited)
            unvisited.difference_update(adjacent)
            queue.extend((new_node, distance + 1) for new_node in adjacent)
        return -1
