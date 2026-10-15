//
// Created by Germain Jones on 16/09/2026.
//

#ifndef NEETCODE_SEARCHA2DMATRIX_H
#define NEETCODE_SEARCHA2DMATRIX_H
#include <vector>

class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int> > &matrix, int target) {
        const size_t rows{matrix.size()};
        const size_t columns{matrix[0].size()};
        size_t left{0};
        size_t right{rows * columns};

        while (left < right) {
            const size_t middle{left + (right - left) / 2};
            const auto [row, column] = lengthToSizes(middle, columns);
            const auto value = matrix[row][column];
            if (value < target) {
                left = middle + 1;
            } else if (value == target) {
                return true;
            } else {
                right = middle;
            }
        }
        return false;
    }

    std::pair<size_t, size_t> lengthToSizes(const size_t length, const size_t columns) {
        return {length / columns, length % columns};
    }
};

#endif //NEETCODE_SEARCHA2DMATRIX_H
