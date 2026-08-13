class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_mult = [0]*len(nums)
        l_mult = [0]*len(nums)
        rmult = 1
        lmult = 1
        for i in range(len(nums)):
           j = -i -1
           r_mult[i] = rmult
           rmult *= nums[i]
           l_mult[j] = lmult
           lmult *= nums[j]
           
        return [i*j for i,j in zip(r_mult, l_mult)]
