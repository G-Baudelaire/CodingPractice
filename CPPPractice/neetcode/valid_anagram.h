//
// Created by germa_ on 13/08/2026.
//

#ifndef NEETCODE_VALIDANAGRAM_H
#define NEETCODE_VALIDANAGRAM_H
#include <algorithm>
#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        std::ranges::sort(s);
        std::ranges::sort(t);
        return s == t;
    }
};

#endif //NEETCODE_VALIDANAGRAM_H
