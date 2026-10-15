//
// Created by Germain Jones on 15/08/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION202_H
#define LEETCODEPRACTICE_SOLUTION202_H
#include <iostream>
#include <ostream>
#include <unordered_set>

class Solution202 {
public:
  bool isHappy(int n) {
    std::unordered_set<int> set;

    while (n != 1) {
      if (set.contains(n)) return false;
      set.insert(n);
      n = iterate(n);
      std::cout << n << std::endl;
    }

    return true;
  }

  int iterate(int number) {
    int sum = 0;

    while (number != 0) {
      const int digit = number % 10;
      sum += digit * digit;
      number /= 10;
    }

    return sum;
  }
};
#endif //LEETCODEPRACTICE_SOLUTION202_H
