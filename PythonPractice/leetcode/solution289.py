# Game of Life
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        flip = list()

        for row in range(len(board)):
            for column in range(len(board[0])):
                summation = self.get_sum_of_neighbours(board, row, column)
                if (not board[row][column] and summation == 3) or (board[row][column] and not 2 <= summation <= 3):
                    flip.append((row, column))

        for row, column in flip:
            if board[row][column]:
                board[row][column] = 0
            else:
                board[row][column] = 1
    def get_sum_of_neighbours(self, board, row, column):
        m = len(board)  # number of rows
        n = len(board[0]) if m > 0 else 0  # number of columns

        # List of relative neighbor positions
        neighbour_positions = [
            (-1, -1), (-1, 0), (-1, +1),
            (0, -1), (0, +1),
            (+1, -1), (+1, 0), (+1, +1)
        ]
        summation = 0

        for dr, dc in neighbour_positions:
            r, c = row + dr, column + dc
            if 0 <= r < m and 0 <= c < n:  # Check if within bounds
                summation += board[r][c]

        return summation

if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(board)
    print(board)
