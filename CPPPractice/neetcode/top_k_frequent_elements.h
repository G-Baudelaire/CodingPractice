//
// Created by germa_ on 16/08/2026.
//

#ifndef NEETCODE_TOPKFREQUENTELEMENTS_H
#define NEETCODE_TOPKFREQUENTELEMENTS_H
#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int> &nums, int k) {
        std::unordered_map<int, int> counts;
        for (int number: nums) {
            counts[number]++;
        }

        std::vector<std::pair<int, int> > countVec(counts.begin(), counts.end());
        std::ranges::sort(countVec, std::greater{}, &std::pair<int, int>::second);

        std::vector<int> result;
        for (int i = 0; i < k; ++i) {
            result.push_back(countVec[i].first);
        }
        return result;
    }
};
#endif //NEETCODE_TOPKFREQUENTELEMENTS_H
