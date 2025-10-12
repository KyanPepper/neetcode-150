class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wordset = {}
        for c in s:
            if c in wordset:
                wordset[c]+=1
            else: 
                wordset[c] = 1

        for c in t:
            if c not in wordset:
                return False
            
            wordset[c]-=1
            if wordset[c] < 0:
                return False
        return True




        