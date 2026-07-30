class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        counter = 1
        while counter<len(nums):
            if nums[counter-1] == nums[counter]:
                
                return True
            else:
                
                counter +=1
        return False