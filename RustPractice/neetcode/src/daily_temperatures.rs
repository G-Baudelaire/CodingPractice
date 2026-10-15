pub struct Solution;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut result = vec![0; temperatures.len()];
        let mut stack = Vec::new();
        for (index, &temperature) in temperatures.iter().enumerate() {
            while let Some(&(i, t)) = stack.last() {
                if t < temperature {
                    stack.pop();
                    let days_until_warmer_temperature = index - i;
                    result[i] = days_until_warmer_temperature as i32;
                } else {
                    break;
                }
            }
            stack.push((index, temperature))
        }
        result
    }
}
