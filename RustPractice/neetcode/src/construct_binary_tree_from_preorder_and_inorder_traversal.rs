use std::cell::RefCell;
use std::cmp::PartialEq;
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
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::new_inner(&preorder, &inorder)
    }

    fn new_inner(preorder: &[i32], inorder: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        let root = *preorder.first()?;
        let closure = |&index: &usize| inorder[index] == root;
        let mid = (0..inorder.len()).find(closure)?;
        let left = Self::new_inner(&preorder[1..mid + 1], &inorder[..mid]);
        let right = Self::new_inner(&preorder[mid + 1..], &inorder[mid + 1..]);
        let tree_node = TreeNode {
            val: root,
            left,
            right,
        };
        Some(Rc::new(RefCell::new(tree_node)))
    }
}
