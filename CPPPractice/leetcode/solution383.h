//
// Created by Germain Jones on 02/08/2025.
//

#ifndef SOLUTION383_H
#define SOLUTION383_H
#include <iostream>
#include <ostream>
#include <string>
#include <bits/stdc++>
using namespace std;

class Solution383 {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (magazine.length() < ransomNote.length()) return false;

        int charCount[26] = {0};

        for (char magazineChar: magazine) { charCount[magazineChar - 'a']++; }
        for (char ransomChar: ransomNote) { charCount[ransomChar - 'a']--; }

        for (int count: charCount) { if (count < 0) return false; }
        return true;
    }
};
#endif //SOLUTION383_H
