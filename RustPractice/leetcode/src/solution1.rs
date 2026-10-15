use std::collections::HashMap;

pub struct Solution;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, usize> = HashMap::new();

        for (current_idx, &num) in nums.iter().enumerate() {
            let complement = target - num;

            if let Some(&matched_idx) = map.get(&complement) {
                return vec![matched_idx as i32, current_idx as i32];
            }

            map.insert(num, current_idx);
        }

        Vec::new()
    }
}