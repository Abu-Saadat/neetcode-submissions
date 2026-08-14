class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            longest = 1
            num_set = set(nums)
            for num in nums:
                v = num
                streak = 1
                if num - 1 in num_set:
                    continue
                elif num + 1 not in num_set:
                    continue
                else:
                    while v + 1 in num_set:
                        streak += 1
                        v+=1
                    
                    longest = max(streak, longest)
            return longest
        else:
            return 0