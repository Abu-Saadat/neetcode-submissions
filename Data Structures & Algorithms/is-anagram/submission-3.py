class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount, tcount={},{}
        for i in range(len(s)):
            if s[i] not in scount.keys():
                scount[s[i]] = 1
            else:
                scount[s[i]] += 1

            if t[i] not in tcount.keys():
                tcount[t[i]] = 1
            else:
                tcount[t[i]] += 1
        
        if scount == tcount:
            return True
        else: 
            return False

        