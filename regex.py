
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        #nnn #n*
        s_index = 0 #string
        p_index = 0 #regex

        s_len = s.__len__()

        p_len = p.__len__()

        def dfs(s_index,p_index):
            nonlocal s_len
            nonlocal p_len
            nonlocal s
            nonlocal p
            if p_index >= p_len and s_index >= s_len:
                return True
            
            if p_index >= p_len and s_index<=s_len:
                return False
            
            p_val = p[p_index]

            p_star = 'temp'#Throwaway

            x1 = False
            x2 = False
            x3 = False
               #nnn #n*  #nnn #n*
            if p_index+1 < p_len:
                p_star = p[p_index+1]

            if p_star == "*":
                x1 = dfs(s_index+1,p_index) # uses s index for star
                x3 = dfs(s_index,p_index+2) # does nothing with star

            if p_val == "." or s[s_index] == p[p_index]:
                x2 = dfs(s_index+1,p_index+1)
            
            return x1 or x2 or x3
            
        return dfs(0,0)


            
        

                
            

            


