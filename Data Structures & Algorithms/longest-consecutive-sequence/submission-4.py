class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        v = sorted(set(nums))
        num_set = set(nums)
        longest = 0
        curr = 1
        for i in range(len(v)):
            if v[i] + 1 in num_set:
                curr+=1
            else:
                curr = 1
            longest = max(longest, curr)
        return longest
