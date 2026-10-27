struct Solution;

impl Solution {
    pub fn combination_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut current_combination = Vec::new();
        let mut nums = nums;
        nums.sort();
        Self::dfs(&nums, target, &mut result, &mut current_combination, 0, 0);
        result
    }

    fn dfs(
        nums: &Vec<i32>,
        target: i32,
        result: &mut Vec<Vec<i32>>,
        current_combination: &mut Vec<i32>,
        current_sum: i32,
        index: usize,
    ) {
        match target.cmp(&current_sum) {
            std::cmp::Ordering::Less => (),
            std::cmp::Ordering::Equal => result.push(current_combination.clone()),
            std::cmp::Ordering::Greater => Self::dfs_next_indices(
                nums,
                target,
                result,
                current_combination,
                current_sum,
                index,
            ),
        }
    }

    fn dfs_next_indices(
        nums: &Vec<i32>,
        target: i32,
        result: &mut Vec<Vec<i32>>,
        current_combination: &mut Vec<i32>,
        current_sum: i32,
        index: usize,
    ) {
        for i in index..nums.len() {
            let value = nums[i];
            let next_sum = current_sum + value;
            if next_sum < target {
                return;
            }
            current_combination.push(value);
            Self::dfs(nums, target, result, current_combination, next_sum, i);
            current_combination.pop();
        }
    }
}
