# Rotate Imate
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge_length = len(matrix)

        top = 0
        bottom = edge_length - 1

        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1

        for row in range(edge_length):
            for col in range(row + 1, edge_length):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]



if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)