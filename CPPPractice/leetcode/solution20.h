//
// Created by Germain Jones on 30/07/2025.
//

#ifndef SOLUTION20_H
#define SOLUTION20_H
#include <stack>
#include <unordered_map>

class Solution {
public:
  bool isValid(string s) {
    std::stack<char> opening_stack;
    std::unordered_map<char, char> matching{{'(', ')'}, {'[', ']'}, {'{', '}'}};

    for (char character: s) {
      if (character == '(' || character == '{' || character == '[') {
        opening_stack.push(character);
        continue;
      }

      if (opening_stack.empty()) return false;

      char top = opening_stack.top();
      if (matching[top] != character) return false;

      opening_stack.pop();
    }

    return opening_stack.empty();
  }
};

#endif //SOLUTION20_H