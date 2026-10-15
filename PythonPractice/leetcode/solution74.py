# Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target < matrix[0][0] or matrix[-1][-1] < target:
            return False
        elif len(matrix) == 1:
            return self.searchRow(matrix[0], target)
        else:
            half_index = len(matrix) // 2
            return self.searchMatrix(matrix[:half_index], target) or self.searchMatrix(matrix[half_index:], target)

    def searchRow(self, row, target):
        if not row or target < row[0] or row[-1] < target:
            return False
        elif len(row) == 1 and row[0] == target:
            return True
        else:
            half_index = len(row) // 2
            return self.searchRow(row[:half_index],target) or self.searchRow(row[half_index:],target)