from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        #chr 
        def dfs(substr: List[str], index: int):
            if len(substr) >= len(s):
                ispal = self.isPalindrome(substr)
                if ispal:
                    ret.append("".join(substr))

                    
            substr.append(s[index])

            if self.isPalindrome(substr):
                ret.append["".join(substr)]

            index+=1

            dfs(substr, index)


            substr.pop()

            dfs(substr,index)

        
        dfs([],0)
        return ret
                


   
   
   
    def isPalindrome(self, s: str)->bool:
        stack = []
        for i in s:
            stack.append(i)

        if s == "".join(stack):  
            return True
        
        return False






    