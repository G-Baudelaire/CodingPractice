//
// Created by Germain Jones on 2025-09-29.
//

#ifndef LEETCODEPRACTICE_1768_H
#define LEETCODEPRACTICE_1768_H
#include <string>

class Solution {
public:
  std::string mergeAlternately(std::string word1, std::string word2) {
    size_t const len1 = word1.length(), len2 = word2.length();
    std::string result_word;
    size_t pointer1 = 0, pointer2 = 0;

    while (pointer1 < len1 && pointer2 < len2) {
      result_word += word1[pointer1++];
      result_word += word2[pointer2++];
    }

    while (pointer1 < len1) {
      result_word += word1[pointer1++];
    }

    while (pointer2 < len2) {
      result_word += word2[pointer2++];
    }

    return result_word;
  }
};
#endif //LEETCODEPRACTICE_1768_H
