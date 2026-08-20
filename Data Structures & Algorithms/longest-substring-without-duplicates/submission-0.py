class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        res = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
                res = max(res, len(unique))
            else:
                while s[i] in unique:
                    unique.remove(s[l])
                    l+=1
                unique.add(s[i])
        return res
            
            
