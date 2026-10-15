pub struct Solution;

use std::cmp::{max, min};

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut lowest_price = i32::MAX;
        let mut best_profit = i32::MIN;
        for price in prices {
            lowest_price = min(lowest_price, price);
            best_profit = max(best_profit, price - lowest_price);
        }
        best_profit
    }
}
