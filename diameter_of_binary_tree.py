from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ldepth = 0
        rdepth = 0


        def dfs(node: TreeNode):
            if node is None:
                return 0
            
            return max(dfs(node.left),dfs(node.right))+1

        ldepth = dfs(root.left)
        rdepth = dfs(root.right)

        return ldepth +rdepth
        

        