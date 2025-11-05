class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    
class inorder:
    def __init__(self,root:TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def next(self):
        node:TreeNode = self.stack.pop()
        if node.right:
            temp:TreeNode = node.right
            self.stack.append(temp)
            while temp:
                self.stack.append(temp)
                temp=temp.left
        return node
            


    def hasNext(self):
        if self.stack:
            return True


class preorder:
    def __init__(self, root:TreeNode):
        self.stack = [root]

    def next(self):
        node = self.stack.pop()
        if node.right is not None:
            self.stack.append(node.right)
        if node.left is not None:
            self.stack.append(node.left)

        return node

    def hasNext(self):
        if self.stack:
            return True
        


class postorder:
    def __init__(self):
        self.stack = []
    def next(self):
        pass

    def hasNext(self):
        if self.stack:
            return True
        
def test_preorder_returns_correct():
    #arrange
    root = TreeNode(3)
    left = TreeNode(2)
    right = TreeNode(5)
    root.left = left
    root.right = right
    ll = TreeNode(1)
    left.left = ll

    tree = preorder(root)

    #act/assert 
    assert 3 ==  tree.next().val
    assert 2 == tree.next().val
    assert 1 == tree.next().val
    assert 5 == tree.next().val


def test_inorder_returns_correct():
    #arrange
    root = TreeNode(3)
    left = TreeNode(2)
    right = TreeNode(5)
    root.left = left
    root.right = right
    ll = TreeNode(1)
    left.left = ll

    tree = inorder(root)

    #act/assert 
    assert 1 ==  tree.next().val
    assert 2 == tree.next().val
    assert 3 == tree.next().val
    assert 5 == tree.next().val


test_preorder_returns_correct()
test_inorder_returns_correct()


    










        
        
    