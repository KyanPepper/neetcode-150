

from typing import Optional




class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        oldtoNew = {}


        def dfs(node:Node):
            if node in oldtoNew:
                return oldtoNew[node]

            copy = Node(node.val)

            oldtoNew[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))

            return copy
        if node is None:
            return None
            
        return dfs(node)

        