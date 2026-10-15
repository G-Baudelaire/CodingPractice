//
// Created by Germain Jones on 30/07/2025.
//

#ifndef SOLUTION26_H
#define SOLUTION26_H

#include <algorithm>
#include <vector>

class Solution26 {
public:
  int removeDuplicates(std::vector<int> &nums) {
    auto it = std::unique(nums.begin(), nums.end());
    return static_cast<int>(std::distance(nums.begin(), it));
  }
};

};
#endif //SOLUTION26_H