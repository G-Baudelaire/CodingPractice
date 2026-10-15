use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut seen: HashSet<i32> = HashSet::new();
        for number in nums{
            if !seen.insert(number) {return true};
        }
        false
    }
}
