//
// Created by germain on 09/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION1004_H
#define LEETCODEPRACTICE_SOLUTION1004_H
#include <vector>

class Solution {
public:
    int longestOnes(std::vector<int> &nums, int k) {
        int left = -1, right = 0, zeros =0;

        for (; right < nums.size(); right++) {
            zeros += nums[right] == 0;
            if (k < zeros) {
                left++;
                zeros -= nums[left] == 0;
            }
        }
        return right - left - 1;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION1004_H
