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
use std::rc::Rc;

pub struct Solution;

impl Solution {
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        Self::inner_is_same_tree(&p, &q)
    }

    fn inner_is_same_tree(
        p: &Option<Rc<RefCell<TreeNode>>>,
        q: &Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (p, q) {
            (None, None) => true,
            (None, Some(_)) | (Some(_), None) => false,
            (Some(p_reference), Some(q_reference)) => {
                let p_node = p_reference.borrow();
                let q_node = q_reference.borrow();
                p_node.val == q_node.val
                    && Self::inner_is_same_tree(&p_node.left, &q_node.left)
                    && Self::inner_is_same_tree(&p_node.right, &q_node.right)
            }
        }
    }
}
