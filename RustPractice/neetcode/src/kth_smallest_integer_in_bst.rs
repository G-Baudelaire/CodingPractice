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
    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut k = k;
        let result = Self::inner(root, &mut k);
        result.unwrap()
    }

    fn inner(root: Option<Rc<RefCell<TreeNode>>>, k: &mut i32) -> Option<i32> {
        match &root {
            Some(node_reference) => {
                let node = node_reference.borrow();
                if let Some(left_reference) = Self::inner(node.left.clone(), k) {
                    return Some(left_reference);
                }
                *k -= 1;
                if *k == 0 {
                    return Some(node.val);
                }
                Self::inner(node.right.clone(), k)
            }
            None => None,
        }
    }
}
