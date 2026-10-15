pub struct Solution;

impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut combination = vec![];
        let mut result = vec![];
        Self::backtrack(1, n, k, &mut combination, &mut result);
        result
    }

    fn backtrack(i: i32, n: i32, k: i32, combination: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        if i > n {
            return;
        }

        if combination.len() == (k as usize) {
            result.push(combination.clone());
        } else {
            let incremented_i = i + 1;
            combination.push(i);
            Self::backtrack(incremented_i, n, k, combination, result);
            combination.pop();
            Self::backtrack(incremented_i, n, k, combination, result);
        }
    }
}
