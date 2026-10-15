//
// Created by Germain Jones on 17/09/2026.
//

#ifndef NEETCODE_KOKOEATINGBANANAS_H
#define NEETCODE_KOKOEATINGBANANAS_H
#include <algorithm>
#include <numeric>
#include <ranges>
#include <vector>

class Solution {
public:
    int minEatingSpeed(std::vector<int> &piles, int h) {
        auto min = 1;
        auto count = std::ranges::max(piles);

        while (min < max) {
            const auto step = count / 2;
            const auto eating_speed = min + step;
            const auto fn = [this, eating_speed](auto a) -> int { return eatingTime(a, eating_speed); };
            const auto eating_times = piles | std::ranges::views::transform(fn);
            const auto total_eating_time = std::ranges::fold_left(eating_times, 0, std::plus{});

            if (total_eating_time > h) {
                min = eating_speed + 1;
                count -= step + 1;
            } else {
                count = step;
            }
        }
        return min;
    }

    int eatingTime(int pile, int eating_speed) {
        return pile / eating_speed + (pile % eating_speed != 0);
    }
};

#endif //NEETCODE_KOKOEATINGBANANAS_H
