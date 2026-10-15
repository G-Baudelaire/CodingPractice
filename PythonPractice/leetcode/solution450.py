# Definition for a binary tree node.
import itertools
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(val=float("nan"), left=root)
        for node in self.dfs(dummy):
            if node.left and node.left.val == key:
                node.left = self.merge(node.left.left, node.left.right)
                break
            elif node.right and node.right.val == key:
                node.right = self.merge(node.right.left, node.right.right)
                break

        return dummy.left

    def dfs(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            yield node
            stack.append(node.right)
            stack.append(node.left)

    def merge(self, root1, root2):
        merged_tree = None
        for node in itertools.chain(self.dfs(root1), self.dfs(root2)):
            if not merged_tree:
                merged_tree = TreeNode(val=node.val)
                continue

            head = merged_tree
            while True:
                if node.val < head.val and head.left:
                    head = head.left
                elif node.val > head.val and head.right:
                    head = head.right
                elif node.val < head.val and not head.left:
                    head.left = TreeNode(val=node.val)
                    break
                else:
                    head.right = TreeNode(val=node.val)
                    break

        return merged_tree
