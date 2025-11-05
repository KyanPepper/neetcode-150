from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret: List[str] = []

        def dfs(i:int,s:str)->None:
            #leaf nodes
            if(i >= n):
                if self.isValid(s):
                    ret.append(s)
                return 
            
            s1 = s[:]
            s2 = s[:]
            s3 = s[:]
            s4 = s[:]

            s1 += "(("
            s2 += "()"
            s3 += "))"
            s4 += ")("

            dfs(i+1,s1)
            dfs(i+1,s2)
            dfs(i+1,s3)
            dfs(i+1,s4)


        dfs(0, "")
        return ret


    def isValid(self, s:str)->bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            if c == ")":
                #check peak and pop both
                if not stack:
                    return False
                peak = stack.pop()
                
        if len(stack) > 0:
            return False
        return True