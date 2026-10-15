use std::cmp::Ordering;

pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let offset = Self::get_offset(&nums);
        Self::binary_search(&nums, target, offset)
    }

    fn get_offset(nums: &[i32]) -> usize {
        let mut left = 0;
        let mut right = nums.len() - 1;
        while left < right {
            let middle = (left + right) / 2;
            match nums[middle].cmp(&nums[right]) {
                Ordering::Greater => left = middle + 1,
                Ordering::Less | Ordering::Equal => right = middle,
            }
        }
        left
    }

    fn binary_search(nums: &[i32], target: i32, offset: usize) -> i32 {
        let n = nums.len();
        let mut left = offset;
        let mut right = nums.len() + offset;
        while left < right {
            let middle = (left + right) / 2;
            let middle_modulus = middle % n;
            let value = &nums[middle_modulus];
            match target.cmp(value) {
                Ordering::Less => right = middle,
                Ordering::Equal => return middle_modulus as i32,
                Ordering::Greater => left = middle + 1,
            }
        }
        -1
    }
}
