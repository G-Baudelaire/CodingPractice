//
// Created by Germain Jones on 01/08/2025.
//

#ifndef SOLUTION125_H
#define SOLUTION125_H
#include <string>

using namespace std;

class Solution {
public:
  bool isPalindrome(string s) {
    int left_index = 0;
    int right_index = s.size() - 1;

    while (left_index < right_index) {
      while (left_index < right_index && !isalnum(s[left_index])) left_index++;
      while (left_index < right_index && !isalnum(s[right_index])) right_index
          --;
      if (tolower(s[left_index]) != tolower(s[right_index])) return false;
      left_index++;
      right_index--;
    }
    return true;
  }
};
#endif //SOLUTION125_H