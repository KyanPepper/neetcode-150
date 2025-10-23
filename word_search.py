from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])

        def dfs(r,c,i,visited) -> bool:  # CHANGED: return type hint
            nonlocal row_len
            nonlocal col_len
             #true condition
            if i >= len(word):
                return True
                
            #if bound are out return 0
            if (r >= row_len or r < 0 or c >= col_len or c < 0):
                return False
            
            if board[r][c] == word[i]:
                visit_key = (r,c)
                if visit_key in visited:
                    return False
                #right
                visited[visit_key] = True
                right = dfs(r+1,c,i+1,visited)
                #left
                left = dfs(r-1,c,i+1,visited)
                #up
                up = dfs(r,c+1,i+1,visited)
                #down
                down = dfs(r,c-1,i+1,visited)
                #atleast 1 true
                res = right or left or up or down
                if not res:
                    del visited[visit_key]  # CHANGED: backtrack
                return res
            else:
                return False

        for r_index in range(row_len):
            for c_index in range(col_len):   
                if dfs(r_index,c_index,0,{}):
                    return True

        return False
