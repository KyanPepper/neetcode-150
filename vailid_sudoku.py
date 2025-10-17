from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowlen = len(board)
        columnlen = len(board[0])
        rowhash = {}
        colhash = {}
        
        

        for r in range(rowlen):
            for c in range(columnlen):
                num = board[r][c]
                if num in rowhash:
                    return False

                
                colhash.add(c)


        return True 
                
        