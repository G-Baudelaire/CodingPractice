//
// Created by Germain Jones on 13/08/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION392_H
#define LEETCODEPRACTICE_SOLUTION392_H
#include <string>
using std::string;

class Solution {
public:
  bool isSubsequence(string s, string t) {
    int pointer_s = 0, pointer_t = 0;
    while (pointer_s < s.size() && pointer_t < t.size()) {
      if (s[pointer_s] == t[pointer_t]) pointer_s++;
      pointer_t++;
    }
    return pointer_s;
  }
};

#endif //LEETCODEPRACTICE_SOLUTION392_H
