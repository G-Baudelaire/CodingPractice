use std::cmp::Ordering;

pub struct Solution;

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (rows, columns) = (matrix.len(), matrix[0].len());
        let (mut left, mut right) = (0, rows * columns);

        while left < right {
            let middle = left + (right - left) / 2;
            let (row, column) = Self::length_to_matrix_size(middle, columns);
            let value = matrix[row][column];
            match value.cmp(&target) {
                Ordering::Less => left = middle + 1,
                Ordering::Equal => return true,
                Ordering::Greater => right = middle,
            }
        }

        false
    }

    fn length_to_matrix_size(flat_index: usize, columns: usize) -> (usize, usize) {
        (flat_index / columns, flat_index % columns)
    }
}
