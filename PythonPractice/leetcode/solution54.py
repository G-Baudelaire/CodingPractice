class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return self._spiralOrder(matrix, [0, -1], len(matrix[0]), len(matrix))

    def _spiralOrder(self, matrix, current_index, remaining_length, remaining_height):
        matrix_values = list()

        if remaining_height < 1 or remaining_length < 1:
            return matrix_values

        # Move Right
        matrix_values.extend(matrix[current_index[0]][current_index[1] + 1: current_index[1] + remaining_length + 1])
        current_index[1] += remaining_length

        if remaining_height == 1:
            return matrix_values

        # Move Down
        print(current_index, remaining_height)
        matrix_values.extend([matrix[current_index[0] + i][current_index[1]] for i in range(1, remaining_height)])
        current_index[0] += (remaining_height - 1)

        if remaining_length == 1:
            return matrix_values

        # Move Left
        new_values = reversed(matrix[current_index[0]][current_index[1] - (remaining_length - 1): current_index[1]])
        matrix_values.extend(new_values)
        current_index[1] -= (remaining_length - 1)

        # Move Up
        matrix_values.extend([matrix[current_index[0] - i][current_index[1]] for i in range(1, remaining_height - 1)])
        current_index[0] -= (remaining_height - 2)

        return matrix_values + self._spiralOrder(matrix, current_index, remaining_length - 2, remaining_height - 2)


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

print(Solution().spiralOrder(matrix))
