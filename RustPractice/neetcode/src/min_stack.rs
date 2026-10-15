use std::cmp::min;

pub struct MinStack {
    value_stack: Vec<i32>,
    min_stack: Vec<i32>,
}

impl MinStack {
    pub fn new() -> Self {
        MinStack {
            value_stack: Vec::new(),
            min_stack: Vec::new(),
        }
    }

    pub fn push(&mut self, val: i32) {
        let new_minimum = match self.min_stack.last() {
            None => val,
            Some(&previous_max) => min(val, previous_max),
        };
        self.min_stack.push(new_minimum);
        self.value_stack.push(val);
    }

    pub fn pop(&mut self) {
        self.min_stack.pop();
        self.value_stack.pop();
    }

    pub fn top(&self) -> i32 {
        *self.value_stack.last().unwrap()
    }

    pub fn get_min(&self) -> i32 {
        *self.min_stack.last().unwrap()
    }
}

impl Default for MinStack {
    fn default() -> Self {
        Self::new()
    }
}
