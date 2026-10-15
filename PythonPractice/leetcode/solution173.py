from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self._generator = self._in_order_traversal(root)
        self._next_value = self._getNext()

    def _getNext(self):
        try:
            return next(self._generator)
        except StopIteration as e:
            return None

    def next(self) -> int:
        previous_value = self._next_value
        self._next_value = self._getNext()
        return previous_value

    def hasNext(self) -> bool:
        return self._next_value is not None

    def _in_order_traversal(self, root: Optional[TreeNode]):
        if root is None:
            return

        yield from self._in_order_traversal(root.left)
        yield root
        yield from self._in_order_traversal(root.right)
