//
// Created by Germain Jones on 15/08/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION1_H
#define LEETCODEPRACTICE_SOLUTION1_H
#include <unordered_map>
#include <vector>
using namespace std;

class Solution1 {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> matching_value;
    for (int i = 0; i < nums.size(); i++) {
      if (matching_value.contains(nums[i])) {
        return {i, matching_value[nums[i]]};
      }
      matching_value[target - nums[i]] = i;
    }
    return {-1, -1};
  }
};
#endif //LEETCODEPRACTICE_SOLUTION1_H
