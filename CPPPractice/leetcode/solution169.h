//
// Created by Germain Jones on 30/07/2025.
//

#ifndef SOLUTION169_H
#define SOLUTION169_H

#include <vector>

using std::vector;

class Solution169 {
public:
  int majorityElement(vector<int> &nums) {
    int majority;
    int count = 0;

    for (int num: nums) {
      if (count == 0) {
        majority = num;
        count++;
      } else if (num == majority) {
        count++;
      } else {
        count--;
      }
    }

    return majority;
  }
};
#endif //SOLUTION169_H