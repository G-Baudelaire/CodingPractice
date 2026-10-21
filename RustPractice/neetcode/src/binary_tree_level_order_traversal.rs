#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

struct Solution;

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut queue: VecDeque<_> = VecDeque::new();
        if let Some(r) = root {
            queue.push_back(r);
        }

        while !queue.is_empty() {
            let mut level_values = Vec::with_capacity(queue.len());
            for _ in 0..queue.len() {
                let node_reference = queue.pop_front().unwrap();
                let node = node_reference.borrow();
                level_values.push(node.val);
                if let Some(l) = &node.left {
                    queue.push_back(l.clone());
                }
                if let Some(r) = &node.right {
                    queue.push_back(r.clone());
                }
            }
            result.push(level_values);
        }

        result
    }
}
