#pragma once

#include <algorithm>
#include <cstddef>
#include <numeric>
#include <vector>
class Solution {
public:
  int candy(std::vector<int> &ratings) {
    if (ratings.empty()) {
      return 0;
    }

    std::vector<int> candies(ratings.size(), 1);
    leftPass(ratings, candies);
    rightPass(ratings, candies);
    return std::reduce(candies.begin(), candies.end(), 0);
  }

  void leftPass(const std::vector<int> &ratings, std::vector<int> &candies) {
    std::size_t secondFromLeftIndex = 1;
    for (std::size_t i{secondFromLeftIndex}; i < candies.size(); i++) {
      std::size_t leftIndex = i - 1;
      if (ratings[leftIndex] < ratings[i]) {
        candies[i] = candies[leftIndex] + 1;
      }
    }
  }

  void rightPass(const std::vector<int> &ratings, std::vector<int> &candies) {
    int secondFromRightIndex = candies.size() - 2;
    for (int i{secondFromRightIndex}; i >= 0; i--) {
      int rightIndex = i + 1;
      if (ratings[rightIndex] < ratings[i]) {
        candies[i] = std::max(candies[i], candies[rightIndex] + 1);
      }
    }
  }
};
