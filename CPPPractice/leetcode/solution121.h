//
// Created by Germain Jones on 31/07/2025.
//

#ifndef SOLUTION121_H
#define SOLUTION121_H

#include <vector>
using std::vector;

class Solution121 {
public:
  int maxProfit(vector<int> &prices) {
    if (prices.size() < 2) return 0;

    int min_price = prices.front();
    int max_profit = 0;

    for (int price: prices) {
      min_price = std::min(min_price, price);
      max_profit = std::max(max_profit, price - min_price);
    }
    return max_profit;
  }
};

#endif //SOLUTION121_H