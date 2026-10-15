use leetcode::solution1::Solution as TwoSum;
use neetcode::contains_duplicate::Solution as ContainsDuplicate;

fn main() {
    println!("{:?}", TwoSum::two_sum(vec![2, 7, 11, 15], 9));
    println!("{}", ContainsDuplicate::has_duplicate(vec![1, 2, 3, 3]));
}
