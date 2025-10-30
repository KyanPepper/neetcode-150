from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        adj = {}

        for tup in prerequisites:
            key = tup[1]
            value = tup[0]
            if key in adj:
                adj[key].append(value)
            else:
                adj[key] = [value]

        seen = set()

        def dfs(i:int)->List[int]:
            neighbors:List = adj[i]
            #base case for disjointed
            if len(neighbors) == 0 and i not in seen:
                return [i]
            #case for when node was appended already
            elif len(neighbors) == 0:
                return []
            #in loop
            if i in seen:
                return []

            seen.add(i)

            for nei in neighbors:
                ret = dfs(nei)
                if len(ret) > 0:
                    return ret.append(i)
                else:
                    return []
                
        ret:List[int] = []
        for i in adj.keys():
            ret.extend(dfs(i))

        return ret






                
                

        

            
        
        
        