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

struct NodeAttributes {
    depth: usize,
    distance: usize,
}

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::inner_diameter_of_binary_tree(&root).distance as i32
    }

    fn inner_diameter_of_binary_tree(root: &Option<Rc<RefCell<TreeNode>>>) -> NodeAttributes {
        match root {
            Some(reference) => {
                let node = reference.borrow();
                let left_attributes = Self::inner_diameter_of_binary_tree(&node.left);
                let right_attributes = Self::inner_diameter_of_binary_tree(&node.right);
                let depth = max(left_attributes.depth, right_attributes.depth) + 1;
                let distance = [
                    left_attributes.distance,
                    right_attributes.distance,
                    left_attributes.depth + right_attributes.depth,
                ]
                .iter()
                .fold(0, |a, &b| max(a, b));

                NodeAttributes { depth, distance }
            }

            None => NodeAttributes {
                depth: 0,
                distance: 0,
            },
        }
    }
}
