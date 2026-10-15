//
// Created by germain on 01/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION238_H
#define LEETCODEPRACTICE_SOLUTION238_H
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int> &nums) {
        std::vector<int> output(nums.size(), 1);

        int product = 1;
        for (int i = 0; i < output.size(); i++) {
            output[i] *= product;
            product *= nums[i];
        }

        product = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            output[i] *= product;
            product *= nums[i];
        }

        return output;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION238_H
