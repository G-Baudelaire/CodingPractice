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

pub struct Solution;

impl Solution {
    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        let mut queue = VecDeque::from([root]);
        while let Some(node) = queue.pop_front() {
            if Self::inner_is_subtree(&node, &sub_root) {
                return true;
            }

            if let Some(reference) = node {
                let tree_node = reference.borrow();
                queue.push_back(tree_node.left.clone());
                queue.push_back(tree_node.right.clone());
            }
        }
        false
    }

    fn inner_is_subtree(
        root: &Option<Rc<RefCell<TreeNode>>>,
        sub_root: &Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (root, sub_root) {
            (None, None) => true,
            (Some(reference_a), Some(reference_b)) => {
                let root_a = reference_a.borrow();
                let root_b = reference_b.borrow();
                let is_same_val = root_a.val == root_b.val;
                is_same_val
                    && Self::inner_is_subtree(&root_a.left, &root_b.left)
                    && Self::inner_is_subtree(&root_a.right, &root_b.right)
            }
            _ => false,
        }
    }
}
