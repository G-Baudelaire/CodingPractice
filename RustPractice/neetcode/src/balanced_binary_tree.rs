use std::cell::RefCell;
use std::cmp::max;
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

pub struct Solution;

impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::inner_is_balanced(&root).0
    }

    fn inner_is_balanced(root: &Option<Rc<RefCell<TreeNode>>>) -> (bool, i32) {
        match root {
            Some(node_reference) => {
                let node = node_reference.borrow();
                let (left_balanced, left_height) = Self::inner_is_balanced(&node.left);
                let (right_balanced, right_height) = Self::inner_is_balanced(&node.right);
                let absolute_difference = i32::abs(left_height - right_height);
                let balanced = left_balanced && right_balanced && (absolute_difference <= 1);
                let height = max(left_height, right_height);
                (balanced, height + 1)
            }
            None => (true, 0),
        }
    }
}
