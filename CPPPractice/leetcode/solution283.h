//
// Created by germain on 01/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION283_H
#define LEETCODEPRACTICE_SOLUTION283_H
#include <algorithm>
#include <vector>

class Solution {
public:
    void moveZeroes(std::vector<int> &nums) {
        const auto last = std::ranges::remove(nums, 0).begin();
        std::fill(last, nums.end(), 0);
    }
};

#endif //LEETCODEPRACTICE_SOLUTION283_H
