
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        ret = []
        q.append(root)
        while q:
            length = len(q)
            sublist = []
            for i in range(length):
                node: TreeNode = q.popleft()
                if node.left is not None:
                  q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                sublist.append(node.val)
            ret.append(sublist)
        return ret



                

            