use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

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

struct Solution;

impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        Self::visit(root, 0, &mut result);
        result
    }

    fn visit(node: Option<Rc<RefCell<TreeNode>>>, depth: usize, result: &mut Vec<i32>) {
        let Some(node) = node else { return };
        let node = node.borrow();

        if depth == result.len() {
            result.push(node.val);
        }
        Self::visit(node.right.clone(), depth + 1, result);
        Self::visit(node.left.clone(), depth + 1, result);
    }
}
