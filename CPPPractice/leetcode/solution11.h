//
// Created by germain on 01/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION11_H
#define LEETCODEPRACTICE_SOLUTION11_H
#include <vector>

class Solution {
public:
    int maxArea(std::vector<int> &height) {
        size_t left = 0, right = height.size() - 1;
        int max_volume = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                max_volume = std::max(max_volume, height[left] * static_cast<int>(right - left));
                left++;
            } else {
                max_volume = std::max(max_volume, height[right] * static_cast<int>(right - left));
                right--;
            }
        }

        return max_volume;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION11_H
