//
// Created by Germain Jones on 16/09/2026.
//

#ifndef NEETCODE_DAILYTEMPERATURES_H
#define NEETCODE_DAILYTEMPERATURES_H
#include <stack>
#include <vector>
#include <ranges>

class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int> &temperatures) {
        std::stack<std::pair<size_t, int> > stack{};
        std::vector<int> results(temperatures.size(), 0);

        for (auto [index, temperature]: std::views::enumerate(temperatures)) {
            while (true) {
                if (stack.empty()) break;
                auto [top_index, top_temperature] = stack.top();
                if (top_temperature <= temperature) break;
                stack.pop();
                results[top_index] = index - top_index;
            }
            stack.push({index, temperature});
        }
        return results;
    }
};

#endif //NEETCODE_DAILYTEMPERATURES_H
