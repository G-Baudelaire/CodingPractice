//
// Created by germain on 09/10/2025.
//

#ifndef LEETCODEPRACTICE_2215_H
#define LEETCODEPRACTICE_2215_H
#include <algorithm>
#include <set>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int> > findDifference(vector<int> &nums1, vector<int> &nums2) {
        std::set<int> mset1(nums1.begin(), nums1.end()), mset2(nums2.begin(), nums2.end());
        vector<int> result1, result2;

        std::ranges::set_difference(mset1, mset2, std::inserter(result1, result1.begin()));
        std::ranges::set_difference(mset2, mset1, std::inserter(result2, result2.begin()));

        return {result1, result2};
    }
};
#endif //LEETCODEPRACTICE_2215_H
