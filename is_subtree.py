
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not (root and subRoot):
            return False

        node = root
        while node:
            nleft = node.left
            nright = node.right

            if nleft and nleft.val > subRoot.val:
                node = nleft
                continue

            if nright and nright.val > subRoot.val:
                node = nright
                continue

            if 

            #Sub function
        def isSameTree(p,q):
                if p is None and q is None:
                    return True
            
                if p is None and q is not None:
                    return False
            
                if q is None and p is not None:
                    return False
                
                if p.val != q.val:
                    return False
                
                left = self.isSameTree(p.left,q.left)
                right = self.isSameTree(p.right,q.right)

                return left and right

     
        
        return isSameTree(node.left,node.right)
            

        