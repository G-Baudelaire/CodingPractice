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

struct Solution;

impl Solution {
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::count_good(root, i32::MIN)
    }

    fn count_good(root: Option<Rc<RefCell<TreeNode>>>, max_so_far: i32) -> i32 {
        let Some(node) = root else {
            return 0;
        };
        let node = node.borrow();
        let is_good = node.val >= max_so_far;
        let new_max = max_so_far.max(node.val);

        i32::from(is_good)
            + Self::count_good(node.left.clone(), new_max)
            + Self::count_good(node.right.clone(), new_max)
    }
}
