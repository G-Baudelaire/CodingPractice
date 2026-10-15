use std::cell::RefCell;
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
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::inner_invert_tree(&root);
        root
    }

    pub fn inner_invert_tree(root: &Option<Rc<RefCell<TreeNode>>>) {
        if let Some(node) = root {
            let mut node_reference = node.borrow_mut();
            let left = node_reference.left.take();
            Self::inner_invert_tree(&left);
            let right = node_reference.right.take();
            Self::inner_invert_tree(&right);
            (node_reference.left, node_reference.right) = (right, left);
        }
    }
}
