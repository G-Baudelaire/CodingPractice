//
// Created by germain on 01/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION1679_H
#define LEETCODEPRACTICE_SOLUTION1679_H
#include <algorithm>
#include <vector>

class Solution {
public:
    int maxOperations(std::vector<int> &nums, int k) {
        std::ranges::sort(nums);
        int left = 0, right = nums.size() - 1;
        int count = 0;

        while (left < right) {
            const int sum = nums[left] + nums[right];
            if (sum == k) {
                count++;
                left++;
                right--;
            } else if (sum < k) {
                left++;
            } else {
                right--;
            }
        }

        return count;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION1679_H
