//
// Created by Germain Jones on 30/07/2025.
//

#ifndef SOLUTION9_H
#define SOLUTION9_H


class Solution9 {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;

        int working_value = x;
        int reverse_value = 0;

        while (working_value != 0) {
            reverse_value *= 10;
            reverse_value += working_value % 10;
            working_value /= 10;
        }

        return x == reverse_value;
    }
};


#endif //SOLUTION9_H
