//
// Created by Germain Jones on 15/09/2026.
//

#ifndef NEETCODE_EVALUATEREVERSEPOLISHNOTATION_H
#define NEETCODE_EVALUATEREVERSEPOLISHNOTATION_H
#include <functional>
#include <stack>
#include <vector>
#include <ranges>

using BinaryFunction = std::function<int(int, int)>;

class Solution {
public:
    int evalRPN(std::vector<std::string> &tokens) {
        std::stack<int> integers;

        for (const auto &token: tokens) {
            int integer;
            if (token == "+" | token == "-" | token == "*" | token == "/") {
                const int right = get_top_and_pop(integers);
                const int left = get_top_and_pop(integers);
                const BinaryFunction binary_function = get_operation(token);
                integer = binary_function(left, right);
            } else {
                integer = std::stoi(token);
            }
            integers.push(integer);
        }

        return integers.top();
    }

    static int get_top_and_pop(std::stack<int> &s) {
        const int i = s.top();
        s.pop();
        return i;
    }

    static BinaryFunction get_operation(const std::string &operation) {
        if (operation == "+") return std::plus{};
        if (operation == "-") return std::minus{};
        if (operation == "*") return std::multiplies{};
        return std::divides{};
    }
};

#endif //NEETCODE_EVALUATEREVERSEPOLISHNOTATION_H
