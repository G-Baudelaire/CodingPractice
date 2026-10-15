pub struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        for c in s.chars() {
            match c {
                '(' | '[' | '{' => stack.push(c),
                ')' | ']' | '}' => {
                    let expected = Self::get_opener(c);
                    if stack.pop() != Some(expected) {
                        return false;
                    }
                }
                _ => Self::panic_unexpected_char(c),
            }
        }
        stack.is_empty()
    }

    fn get_opener(c: char) -> char {
        match c {
            ')' => '(',
            ']' => '[',
            '}' => '{',
            _ => Self::panic_unexpected_char(c),
        }
    }

    fn panic_unexpected_char(c: char) -> ! {
        panic!("Unexpected Character: {}", c)
    }
}
