//
// Created by Germain Jones on 02/08/2025.
//

#ifndef SOLUTION205_H
#define SOLUTION205_H
#include <string>
using namespace std;

class Solution205 {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) return false;

        int s_sighted[256] = {0};
        int t_sighted[256] = {0};

        for (int i = 0; i < s.size(); i++) {
            if (s_sighted[s[i]] != t_sighted[t[i]]) return false;
            s_sighted[s[i]] = i + 1;
            t_sighted[t[i]] = i + 1;
        }

        return true;
    }
};
#endif //SOLUTION205_H
