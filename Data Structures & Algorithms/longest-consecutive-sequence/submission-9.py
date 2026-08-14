class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                streak = 1
                curr = num
                while curr + 1 in num_set:
                    streak += 1
                    curr+=1
                longest = max(streak, longest)
        return longest