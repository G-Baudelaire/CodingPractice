use std::cmp::min;

pub struct Solution;

impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut t2 = 0;
        let mut t1 = 0;

        for price in cost {
            let total_cost = min(t2, t1) + price;
            t2 = t1;
            t1 = total_cost;
        }

        min(t2, t1)
    }
}
