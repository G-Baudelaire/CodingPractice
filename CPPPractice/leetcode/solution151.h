//
// Created by Germain Jones on 03/09/2025.
//

#ifndef SOLUTION151_H
#define SOLUTION151_H
#include <stack>
#include <string>

using std::string;

class Solution {
public:
    string reverseWords(string s) {
        std::stack<string> words;

        auto pointer = s.find(' ');
        while (pointer != string::npos) {
            string substring = s.substr(0, pointer);
            if (!substring.empty()) words.push(substring);
            s.erase(0, substring.length() + 1);
            pointer = s.find(' ');
        }
        if (!s.empty()) words.push(s);
        string result;

        while (!words.empty()) {
            if (!result.empty()) result.push_back(' ');
            result.append(words.top());
            words.pop();
        }

        return result;
    }
};
#endif //SOLUTION151_H
