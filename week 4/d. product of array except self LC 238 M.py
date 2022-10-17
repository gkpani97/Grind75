class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_0 = 0
        for i in nums:
            if i == 0:
                count_0 += 1
            else:
                product = product * i
        
        if not count_0:
            return [product// i for i in nums]
        else:
            if count_0 > 1:
                return [0] * len(nums)
            else:
                return [0 if i != 0 else product for i in nums]
