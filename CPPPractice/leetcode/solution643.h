//
// Created by germain on 09/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION643_H
#define LEETCODEPRACTICE_SOLUTION643_H
#include <numeric>
#include <vector>

class Solution {
public:
    double findMaxAverage(std::vector<int> &nums, int k) {
        int total = std::reduce(nums.begin(), nums.begin() + k, 0);
        int max_total = total;

        for (int i = k; i < nums.size(); i++) {
            total += nums[i] - nums[i - k];
            max_total = std::max(max_total, total);
        }
        return static_cast<double>(max_total) / k;
    }
};

#endif //LEETCODEPRACTICE_SOLUTION643_H
