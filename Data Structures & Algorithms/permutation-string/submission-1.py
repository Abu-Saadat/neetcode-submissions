class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = [0]*26
        s2_count = [0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-97] += 1
        l = 0
        for r in range(len(s2)):
            s2_count[ord(s2[r])-97] += 1
            while s1_count != s2_count and r-l+1 > len(s1) -1:
                s2_count[ord(s2[l])-97] -= 1
                l+=1
                      
            if s2_count == s1_count:
               return True
        return False