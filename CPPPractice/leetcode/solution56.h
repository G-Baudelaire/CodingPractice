//
// Created by Germain Jones on 31/07/2025.
//

#ifndef SOLUTION56_H
#define SOLUTION56_H

#include <string>
using std::string;

class Solution56 {
public:
  int lengthOfLastWord(string s) {
    // 1) find the last non-space character
    auto end = s.find_last_not_of(' ');
    if (end == std::string::npos) return 0;

    // 2) find the space immediately before that word
    auto start = s.find_last_of(' ', end);

    // 3) distance between them is the length:
    //    if start==npos, (end - npos) underflows to end+1 as desired
    return static_cast<int>(end - start);
  }
};
#endif //SOLUTION56_H