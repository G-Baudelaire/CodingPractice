//
// Created by Germain Jones on 15/09/2026.
//

#ifndef NEETCODE_MINSTACK_H
#define NEETCODE_MINSTACK_H
#include <stack>

class MinStack {
public:
    MinStack() {
    }

    void push(int val) {
        const int minimum = min_stack.empty() ? val : std::min(val, min_stack.top());
        min_stack.push(minimum);
        value_stack.push(val);
    }

    void pop() {
        value_stack.pop();
        min_stack.pop();
    }

    int top() {
        return value_stack.top();
    }

    int getMin() {
        return min_stack.top();
    }

private:
    std::stack<int> value_stack;
    std::stack<int> min_stack;
};

#endif //NEETCODE_MINSTACK_H
