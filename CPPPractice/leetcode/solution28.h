//
// Created by Germain Jones on 01/08/2025.
//

#ifndef SOLUTION28_H
#define SOLUTION28_H
#include <string>

using namespace std;

class Solution28 {
public:
  // int strStr(string haystack, string needle) {
  //     if (needle.length() > haystack.length()) return -1;
  //
  //     for (int i = 0; i < haystack.length() - needle.length() + 1; ++i) {
  //         if (haystack.substr(i, needle.length()) == needle) {
  //             return i;
  //         }
  //     }
  //     return -1;
  // }
  int strStr(string haystack, string needle) {
    string::size_type position = haystack.find(needle);
    return (position == std::string::npos) ? -1 : static_cast<int>(position);
  }
};
#endif //SOLUTION28_H