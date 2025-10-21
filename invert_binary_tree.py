
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root : TreeNode):
            if root is None:
                return
            tempLeft = root.left
            root.left = root.right
            root.right = tempLeft
            dfs(root=root.right)
            dfs(root=root.left)
            
        dfs(root)

        return root
        

                
            

        

        