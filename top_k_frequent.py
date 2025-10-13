from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqhash = {}
        for num in nums:
            if num not in freqhash:
                freqhash[num] = 1
            else:
                freqhash[num]+=1 


        sorted_items = sorted(freqhash.items(), key=lambda x: x[1], reverse=True)

        ret = []

        for i in range(k):
            ret.append(sorted_items[i])

        return ret

        