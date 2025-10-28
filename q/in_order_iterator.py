
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return bool(self.stack)
    


class BSTPreorderIterator:
    def __init__(self, root):
        self.stack = []
        if root:
            self.stack.append(root)

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        val = node.val
        # push right first so left is processed next
        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)
        return val


class BSTPostorderIterator:
    def __init__(self, root):
        self.stack = []
        self.last_visited = None
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        while self.stack:
            peek = self.stack[-1]
            # go right if not visited
            if peek.right and self.last_visited != peek.right:
                self._push_left(peek.right)
            else:
                self.last_visited = self.stack.pop()
                return self.last_visited.val
