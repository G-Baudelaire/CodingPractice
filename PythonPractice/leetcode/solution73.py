# Set Matrix Zeros
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_height = len(matrix)
        matrix_width = len(matrix[0])

        zero_columns = [False] * matrix_width
        for m in range(matrix_height):
            zero_in_row = False

            for n  in range(matrix_width):
                if matrix[m][n] == 0:
                    zero_in_row = True
                    zero_columns[n] = True

            if zero_in_row:
                matrix[m] = [0] * matrix_width

        for column in range(matrix_width):
            if zero_columns[column]:
                for row in range(matrix_height):
                    matrix[row][column] =  0

if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    print(matrix)