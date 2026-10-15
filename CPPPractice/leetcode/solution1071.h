//
// Created by Germain Jones on 2025-09-29.
//

#ifndef LEETCODEPRACTICE_1071_H
#define LEETCODEPRACTICE_1071_H
#include <numeric>
#include <string>

class Solution {
public:
  std::string gcdOfStrings(std::string str1, std::string str2) {
    if (str1 + str2 == str2 + str1) {
      int const greatest_common_divisor = std::gcd(str1.length(), str2.length());
      return str1.substr(0, greatest_common_divisor);
    }
    return "";
  }
};
#endif //LEETCODEPRACTICE_1071_H
