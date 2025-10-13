from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqhash = {}
        for num in nums:
            if num not in freqhash:
                freqhash[num] = 1
            else:
                freqhash[num]+=1 
        ret = []
        sorted_list = []
        for i in freqhash.items():
            sorted_list.append((i[1],i[0]))
        sorted_list.sort(reverse=True)
        for i in range(k):
            ret.append(sorted_list[i][1])
        return ret
        

            
    
        