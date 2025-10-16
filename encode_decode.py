from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        if nums is None:
            return []
        
        sum_nums = 1
        product_with_zero=1
        num_of_zeros = 0
        for i in nums:
            sum_nums = sum_nums * i
            if i == 0:
                num_of_zeros = num_of_zeros +1
                continue
            product_with_zero = product_with_zero * i
           

        
        if num_of_zeros > 1:
            return [0] * len(nums)


        for i in nums:
            if i == 0:
                res.append(product_with_zero)
            else:
                res.append(sum_nums//i)
        return res
            
        
            


