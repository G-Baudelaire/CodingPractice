#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

pub struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut previous: Option<Box<ListNode>> = None;
        let mut pointer = head;
        loop {
            match pointer {
                None => break,
                Some(mut node) => {
                    let temporary = node.next;
                    node.next = previous;
                    previous = Some(node);
                    pointer = temporary;
                }
            }
        }
        previous
    }
}
