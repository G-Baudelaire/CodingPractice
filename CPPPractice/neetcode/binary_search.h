//
// Created by Germain Jones on 16/09/2026.
//

#ifndef NEETCODE_BINARYSEARCH_H
#define NEETCODE_BINARYSEARCH_H
#include <vector>

class Solution {
public:
    int search(std::vector<int> &nums, int target) {
        size_t left{0}, right{nums.size()};
        while (left < right) {
            const size_t middle = left + (right - left) / 2;
            const int value = nums[middle];
            if (value < target) {
                left = middle + 1;
            } else if (value == target) {
                return static_cast<int>(middle);
            } else {
                right = middle;
            }
        }
        return -1;
    }
};
#endif //NEETCODE_BINARYSEARCH_H
