//
// Created by Germain Jones on 2025-09-29.
//

#ifndef LEETCODEPRACTICE_605_H
#define LEETCODEPRACTICE_605_H
#include <iostream>
#include <ostream>
#include <vector>

class Solution {
public:
  bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
    size_t const last_value = flowerbed.size() - 1;
    size_t i = 0;
    while (i < flowerbed.size() && 0 < n) {
      if (flowerbed[i] == 1) {
        i++;
        continue;
      }

      bool const left = i == 0 || flowerbed[i - 1] == 0;
      bool const right = i == last_value || flowerbed[i + 1] == 0;

      if (left && right) {
        flowerbed[i] = 1;
        n--;
      }

      i++;
    }
    return n == 0;
  }
};
#endif //LEETCODEPRACTICE_605_H
