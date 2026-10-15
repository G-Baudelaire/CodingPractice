use std::cmp::Ordering;
pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len();
        while left < right {
            let middle = left + (right - left) / 2;
            let potential_value = nums[middle];
            match potential_value.cmp(&target) {
                Ordering::Less => left = middle + 1,
                Ordering::Equal => return middle as i32,
                Ordering::Greater => right = middle,
            }
        }

        -1
    }
}
