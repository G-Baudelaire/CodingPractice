//
// Created by Germain Jones on 2025-09-29.
//

#ifndef LEETCODEPRACTICE_1431_H
#define LEETCODEPRACTICE_1431_H
#include <algorithm>
#include <vector>

class Solution {
public:
  std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
    int const max_candies = *std::ranges::max_element(candies);
    std::vector<bool> result(candies.size());

    for (int i = 0; i < candies.size(); i++) {
      result[i] = max_candies <= candies[i] + extraCandies;
    }

    return result;
  }
};
#endif //LEETCODEPRACTICE_1431_H
