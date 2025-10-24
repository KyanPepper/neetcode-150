from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        cache = [-1] * length
        def dfs(i):

            if i >= length:
                return 0
            if cache[i] != -1:
                return cache[i]
            val = nums[i]
            cache[i] = val + max(dfs(i+2),dfs(i+3))

            return cache[i]


        return max(dfs(0),dfs(1))
        