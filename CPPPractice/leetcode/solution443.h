//
// Created by germain on 01/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION443_H
#define LEETCODEPRACTICE_SOLUTION443_H
#include <string>
#include <vector>

class Solution {
public:
    int compress(std::vector<char> &chars) {
        int write_pointer = 0;

        for (int i = 0; i < chars.size(); ) {
        int count = 0;
        char character = chars[i];
            while (i < chars.size() && character == chars[i]) {
                count++;
                i++;
            }

            chars[write_pointer++] = character;
            if (count > 1) {
                for (const char c: std::to_string(count)) {
                    chars[write_pointer++] = c;
                }
            }
        }

        return write_pointer;
    }
};
#endif //LEETCODEPRACTICE_SOLUTION443_H
