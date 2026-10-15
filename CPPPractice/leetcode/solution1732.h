//
// Created by germain on 09/10/2025.
//

#ifndef LEETCODEPRACTICE_1732_H
#define LEETCODEPRACTICE_1732_H
#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

class Solution {
public:
    int largestAltitude(std::vector<int> &gain) {
        std::partial_sum(gain.begin(), gain.end(), gain.begin());
        return std::max(0, std::ranges::max(gain));
    }
};
#endif //LEETCODEPRACTICE_1732_H
