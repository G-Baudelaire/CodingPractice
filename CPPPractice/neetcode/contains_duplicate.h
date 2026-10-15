//
// Created by germa_ on 13/08/2026.
//

#ifndef NEETCODE_CONTAINSDUPLICATES_H
#define NEETCODE_CONTAINSDUPLICATES_H
#include <set>
#include <vector>

class Solution {
public:
    bool hasDuplicate(std::vector<int> &nums) {
        std::set<int> seen = {};
        for (int number: nums) {
            auto insert = seen.insert(number);
            if (!insert.second) {
                return true;
            }
        }
        return false;
    }
};
#endif //NEETCODE_CONTAINSDUPLICATES_H
