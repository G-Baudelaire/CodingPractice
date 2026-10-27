struct Solution;

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut solution = Vec::new();
        let mut current_subset = Vec::new();
        Self::depth_first_search(&nums, &mut solution, &mut current_subset, 0);
        solution
    }

    fn depth_first_search(
        nums: &Vec<i32>,
        solution: &mut Vec<Vec<i32>>,
        current_subset: &mut Vec<i32>,
        index: usize,
    ) {
        if nums.len() <= index {
            solution.push(current_subset.clone());
            return;
        }

        let value = nums[index];
        current_subset.push(value);
        Self::depth_first_search(nums, solution, current_subset, index + 1);
        current_subset.pop();
        Self::depth_first_search(nums, solution, current_subset, index + 1);
    }
}
