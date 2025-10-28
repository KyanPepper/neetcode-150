
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree_string = []

        def dfs(node:TreeNode):
            if node is None:
                tree_string.append('#')
                tree_string.append(',')
                return 
            

            tree_string.append((str)(node.val))
            tree_string.append(',')
            

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return "".join(tree_string)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_string = data.split(',')
        index = 0


        def dfs() -> Optional[TreeNode]:
            nonlocal index
            if index >= len(tree_string):
                return None
            if tree_string[index] == '#':
                index+=1
                return None
            
            node = TreeNode(tree_string[index])
            index +=1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()

            

            

def test_serialize_returns_preorder():
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.right = TreeNode(3)



    c = Codec()

    string = c.serialize(node)
    print(string + 'printed')
    assert string == '2,1,#,#,3,#,#,'

def test_deserialize_returns_tree():
    string = '2,1,#,#,3,#,#,'

    c = Codec()
    root = c.deserialize(string)

    assert int(root.val) == 2
    assert int(root.left.val) == 1
    assert int(root.right.val) == 3

test_deserialize_returns_tree()
test_serialize_returns_preorder


            
            
            

        
