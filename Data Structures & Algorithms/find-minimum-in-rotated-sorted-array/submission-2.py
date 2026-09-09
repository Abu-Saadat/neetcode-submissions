class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 10001
        l,r = 0, len(nums)-1
        while l<=r:
            if nums[l]<=nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[r] >= nums[m]:
                r = m
            else:
                l = m +1
        
        return res