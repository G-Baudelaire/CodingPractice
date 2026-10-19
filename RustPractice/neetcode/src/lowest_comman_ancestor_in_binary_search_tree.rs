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
use std::cmp::Ordering;
use std::rc::Rc;

pub struct Solution;

impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let mut current_node_option = root;
        let p = p?.borrow().val;
        let q = q?.borrow().val;
        while let Some(node_reference) = current_node_option {
            let node = node_reference.borrow();
            let p_comparison = node.val.cmp(&p);
            let q_comparison = node.val.cmp(&q);
            current_node_option = match (p_comparison, q_comparison) {
                (Ordering::Less, Ordering::Less) => node.right.clone(),
                (Ordering::Greater, Ordering::Greater) => node.left.clone(),
                _ => return Some(node_reference.clone()),
            };
        }

        None
    }
}
