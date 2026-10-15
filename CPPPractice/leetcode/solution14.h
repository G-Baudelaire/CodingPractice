//
// Created by Germain Jones on 31/07/2025.
//

#ifndef SOLUTION14_H
#define SOLUTION14_H

#include <ostream>
#include <string>
#include <vector>
using std::string, std::vector;

class Solution {
public:
  string longestCommonPrefix(vector<string> &strs) {
    //     if (strs.size() == 1) return strs.front();
    //
    //     int matching_length = strs.front().length();
    //     std::cout << matching_length << "\n" << std::endl;
    //     for (int i = 1; i < strs.size(); ++i) {
    //         matching_length = std::min(matching_length, static_cast<int>(strs[i].length()));
    //         while (strs.front().substr(0, matching_length) != strs[i].substr(0, matching_length)) {
    //             matching_length--;
    //             if (matching_length == 0) return "";
    //         }
    //     }
    //     return strs.front().substr(matching_length);
    // }
    if (strs.empty()) return "";

    // find lexicographically smallest and largest strings in one pass
    auto [minIt, maxIt] = std::minmax_element(strs.begin(), strs.end());
    const std::string &a = *minIt;
    const std::string &b = *maxIt;

    // common prefix of only those two covers the whole array
    size_t i = 0, m = std::min(a.size(), b.size());
    while (i < m && a[i] == b[i]) {
      ++i;
    }
    return a.substr(0, i);
  }
};
#endif //SOLUTION14_H