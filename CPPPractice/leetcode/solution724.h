//
// Created by germain on 09/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION724_H
#define LEETCODEPRACTICE_SOLUTION724_H
#include <numeric>
#include <vector>

class Solution {
public:
    int pivotIndex(std::vector<int> &nums) {
        int left_sum = 0;
        int right_sum = std::accumulate(nums.begin(), nums.end(), 0);

        for (int i = 0; i < nums.size(); i++) {
            right_sum -= nums[i];
            if (left_sum == right_sum) return i;
            left_sum += nums[i];
        }

        return -1;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION724_H
