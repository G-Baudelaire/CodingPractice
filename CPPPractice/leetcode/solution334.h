//
// Created by germain on 01/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION334_H
#define LEETCODEPRACTICE_SOLUTION334_H
#include <stddef.h>
#include <vector>

class Solution {
public:
    bool increasingTriplet(std::vector<int> &nums) {
        bool first_found = false, second_found = false;
        int first = 0, second = 0;
        for (const int num: nums) {
            if (!first_found || num <= first) {
                first = num;
                first_found = true;
            } else if (!second_found || num <= second) {
                second = num;
                second_found = true;
            } else {
                return true;
            }
        }
        return false;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION334_H
