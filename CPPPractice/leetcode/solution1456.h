//
// Created by germain on 09/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION1456_H
#define LEETCODEPRACTICE_SOLUTION1456_H
#include <algorithm>
#include <numeric>
#include <string>

class Solution {
public:
    int maxVowels(std::string s, int k) {
        bool isVowel[26] = {false};
        isVowel['a' - 'a'] = true;
        isVowel['e' - 'a'] = true;
        isVowel['i' - 'a'] = true;
        isVowel['o' - 'a'] = true;
        isVowel['u' - 'a'] = true;

        int window_sum = 0;
        for (int i = 0; i < k; i++) window_sum += isVowel[s[i] - 'a'];

        int max_window_sum = window_sum;
        for (int i = k; i < s.size(); i++) {
            window_sum += isVowel[s[i] - 'a'] - isVowel[s[i - k] - 'a'];
            max_window_sum = std::max(max_window_sum, window_sum);
        }
        return max_window_sum;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION1456_H
