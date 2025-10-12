from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i_index, i in enumerate(nums):
            key = target - i
            if key in nummap:
                return [nummap[key], i_index]
            nummap[i] = i_index
        return []

            