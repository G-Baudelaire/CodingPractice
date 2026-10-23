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
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::validate_dfs(root, i32::MIN, i32::MAX)
    }

    fn validate_dfs(root: Option<Rc<RefCell<TreeNode>>>, minimum: i32, maximum: i32) -> bool {
        let Some(node) = root else {
            return true;
        };
        let node = node.borrow();

        node.val > minimum
            && node.val < maximum
            && Self::validate_dfs(node.left.clone(), minimum, node.val)
            && Self::validate_dfs(node.right.clone(), node.val, maximum)
    }
}
