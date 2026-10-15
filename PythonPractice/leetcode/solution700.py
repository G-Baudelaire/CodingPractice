# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        while stack:
            head = stack.pop()
            if head.val == val:
                return head
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)
        return None
