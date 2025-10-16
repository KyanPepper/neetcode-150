from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = set()
        nums = set()
        for i in candidates:
            nums.add(i)

        for i in nums:
            copy = target
            cur = []
            diff = target - i
            cur.append(i)
            while copy > 0:
                

                
        
        
        

