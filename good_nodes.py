class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0
        count = 0
        g = root.val

        def dfs(node: TreeNode, g:int):
            nonlocal count
            if node is None:
                return
            
            if node.val >= g:
                count +=1
                g = node.val
            

            dfs(node.left,g)
            dfs(node.right,g)
            return

        dfs(root,g)
        return count
        

        

            

        