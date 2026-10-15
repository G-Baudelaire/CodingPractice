//
// Created by Germain Jones on 30/07/2025.
//

#ifndef SOLUTION27_H
#define SOLUTION27_H
#include <vector>

class Solution27 {
public:
  int removeElement(vector<int> &nums, int val) {
    auto iterator = std::remove(nums.begin(), nums.end(), val);
    return static_cast<int>(std::distance(nums.begin(), iterator));
  }
};
#endif //SOLUTION27_H