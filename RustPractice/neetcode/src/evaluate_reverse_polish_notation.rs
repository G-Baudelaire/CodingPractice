pub struct Solution;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::with_capacity(tokens.len());

        for token in tokens {
            let integer = Self::get_next_integer(&token, &mut stack);
            stack.push(integer);
        }

        stack.pop().unwrap()
    }

    fn get_next_integer(token: &str, stack: &mut Vec<i32>) -> i32 {
        match token {
            "+" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                left + right
            }
            "-" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                left - right
            }
            "*" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                left * right
            }
            "/" => {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                left / right
            }
            _ => token.parse::<i32>().unwrap(),
        }
    }
}
