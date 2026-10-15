//
// Created by germain on 13/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION67_H
#define LEETCODEPRACTICE_SOLUTION67_H

#include <algorithm>
#include <sstream>
#include <string>
#include <variant>
using std::string;

class Solution {
public:
  string addBinary(string a, string b) {
    if (a.size() < b.size()) {
      std::swap(a, b);
    }

    auto iterator_a = a.rbegin();
    auto iterator_b = b.rbegin();
    bool carry = false;
    std::ostringstream result{};

    auto updateResult = [&result,&carry](const int total) -> void {
      switch (total) {
        case 3:
          result << '1';
          carry = true;
          break;
        case 2:
          result << '0';
          carry = true;
          break;
        case 1:
          result << '1';
          carry = false;
          break;
        default:
          result << '0';
          carry = false;
      }
    };

    while (iterator_b != b.rend()) {
      int total = (*iterator_a == '1') + (*iterator_b == '1') + carry;
      updateResult(total);
      ++iterator_a;
      ++iterator_b;
    }

    while (iterator_a != b.rend()) {
      int total = (*iterator_a == '1') + carry;
      updateResult(total);
      ++iterator_a;
    }

    if (carry) result << '1';

    string r = result.str();
    std::ranges::reverse(r);
    return r;
  }
};
#endif //LEETCODEPRACTICE_SOLUTION67_H
