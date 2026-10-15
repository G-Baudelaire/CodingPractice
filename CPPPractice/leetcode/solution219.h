//
// Created by Germain Jones on 15/08/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION219_H
#define LEETCODEPRACTICE_SOLUTION219_H
#include <unordered_map>
#include <vector>
using namespace std;

class Solution219 {
public:
  bool containsNearbyDuplicate(vector<int> &nums, int k) {
    unordered_map<int, int> value_to_index;

    for (int i = 0; i < nums.size(); i++) {
      if (value_to_index.contains(nums[i])) {
        if ((i - value_to_index[nums[i]]) <= k) {
          return true;
        }
      }
      value_to_index[nums[i]] = i;
    }

    return false;
  }
};
#endif //LEETCODEPRACTICE_SOLUTION219_H
