use std::iter::zip;

pub struct Solution;

impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut stack = Vec::new();
        let mut pairs: Vec<_> = zip(position, speed).collect();
        pairs.sort_by_key(|&(a, _)| a);
        for (pos, spd) in pairs {
            let finish_time: f32 = (target - pos) as f32 / spd as f32;
            Self::update_stack(&mut stack, finish_time);
        }
        stack.len() as i32
    }

    fn update_stack(stack: &mut Vec<f32>, finish_time: f32) {
        while let Some(&t) = stack.last() {
            if t > finish_time {
                break;
            }
            stack.pop();
        }
        stack.push(finish_time)
    }
}
