from collections import deque
class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        
        q = deque()
        i = 0
        ret = ""
        cache = {}

        def dfs(q: deque, i:int)->None:
            nonlocal s
            nonlocal ret
            
            if i >= len(s):
                return None
            
            #append to q
            q.append(s[i])
            key = "".join(q)+str(i)
            
            #return early 
            if key in cache:
                return
            
            sub_string = "".join(q)
            reverse_string = sub_string[::-1]
            if sub_string == reverse_string and len(sub_string) > len(ret):
                ret = sub_string

            #create copy
            copy_pop = q.copy()
            #pop from front since generating substring
            copy_pop.popleft()

            copy = q.copy()
            
            cache[key] = dfs(copy_pop,i+1)
            cache[key] = dfs(copy,i+1)

            return
        
        dfs(q, i)
        return ret
