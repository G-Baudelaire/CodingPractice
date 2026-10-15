//
// Created by Germain Jones on 15/09/2026.
//

#ifndef NEETCODE_VALIDPARENTHESES_H
#define NEETCODE_VALIDPARENTHESES_H
#include <stack>
#include <unordered_map>
#include <vector>


class Solution {
public:
    std::unordered_map<char, char> mapping = {{')', '('}, {']', '['}, {'}', '{'}};

    bool isValid(std::string s) {
        std::stack<char> stack;
        for (char c: s) {
            switch (c) {
                case '(':
                case '{':
                case '[': {
                    stack.push(c);
                    break;
                }
                case ')':
                case '}':
                case ']': {
                    const char opening_char = mapping[c];
                    if (!stack.empty() && stack.top() == opening_char) {
                        stack.pop();
                    } else {
                        return false;
                    }
                    break;
                }
                default:
                    throw;
            }
        }
        return stack.empty();
    }
};

#endif //NEETCODE_VALIDPARENTHESES_H
