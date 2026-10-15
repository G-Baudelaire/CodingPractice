use std::cmp::{max, min};

pub struct Solution;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let maximum_closure = |accumulated: &mut i32, &x| {
            *accumulated = max(*accumulated, x);
            Some(*accumulated)
        };
        let left_maxes: Vec<i32> = height.iter().scan(0, maximum_closure).collect();
        let mut right_maxes: Vec<i32> = height.iter().rev().scan(0, maximum_closure).collect();
        println!("{:?}", left_maxes);
        println!("{:?}", right_maxes);
        right_maxes.reverse();

        let mut output = vec![0; height.len()];
        for (index, &h) in height.iter().enumerate() {
            let left_max = if index == 0 { 0 } else { left_maxes[index - 1] };
            let final_index = height.len() - 1;
            let right_max = if index == final_index {
                0
            } else {
                right_maxes[index + 1]
            };

            let shortest_wall = min(left_max, right_max);
            let water_trapped = max(0, shortest_wall - h);
            output[index] = water_trapped;
        }

        println!("{:?}", output);
        output.iter().sum()
    }
}
