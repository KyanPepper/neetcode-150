from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node):
            if not node:
                result.append("#")
                return
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(result)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))
        def dfs():
            val = next(tokens)
            if val == '#':
                return None
            new_node = TreeNode(int(val))

            new_node.left = dfs()
            new_node.right = dfs()
            return new_node
        return dfs()