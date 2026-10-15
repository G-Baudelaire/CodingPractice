use std::cmp::{Ordering, max};

pub struct Solution;

impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut left_pointer = 0;
        let mut right_pointer = heights.len() - 1;
        let mut max_volume = 0;

        while left_pointer < right_pointer {
            let width = (right_pointer - left_pointer) as i32;
            let left_height = heights[left_pointer];
            let right_height = heights[right_pointer];

            let height = match left_height.cmp(&right_height) {
                Ordering::Less => {
                    left_pointer += 1;
                    left_height
                }
                _ => {
                    right_pointer -= 1;
                    right_height
                }
            };

            let volume = width * height;
            max_volume = max(max_volume, volume);
        }

        max_volume
    }
}
