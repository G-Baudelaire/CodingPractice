//
// Created by germain on 30/09/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION345_H
#define LEETCODEPRACTICE_SOLUTION345_H
#include <set>
#include <stack>

class Solution {
public:
    std::string reverseVowels(std::string s) {
        const std::set vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        size_t left = 0;
        size_t right = s.size() - 1;

        while (left < right) {
            if (vowels.contains(s[left]) && vowels.contains(s[right])) {
                std::swap(s[left], s[right]);
                left++;
                right--;
            } else if (vowels.contains(s[left])) {
                right--;
            } else {
                left++;
            }
        }
        return s;
    }
};
#endif // LEETCODEPRACTICE_SOLUTION345_H
