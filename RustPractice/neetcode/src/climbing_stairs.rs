pub struct Solution;

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut step_minus_1 = 1;
        let mut step = 1;

        for _ in 1..n {
            (step, step_minus_1) = (step + step_minus_1, step);
        }

        step
    }
}
