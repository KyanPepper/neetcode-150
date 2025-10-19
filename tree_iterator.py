
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node: Optional[TreeNode] = root
        self.prev: int = -1
        self.stack: List[TreeNode] = [root]

    def push_left(self, node: TreeNode):
        while node.left != None:
            self.stack.push(node.left)

    def next(self) -> int:
       #if stack is empty return none
       if len(self.stack) == 0:
           return None
       #Push left until leafs are none
       peak = self.stack[-1]
       if peak.left is not None and peak.left.val != self.prev:
            self.push_left(peak)
       popped = self.stack.pop()
       self.prev = popped.val

       #Push right Node
       self.stack.push(popped.right)
        

    def hasNext(self) -> bool:
        if len(self.stack) == 0:
           return False
        return True     


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()