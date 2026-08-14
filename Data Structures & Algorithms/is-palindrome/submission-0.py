class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = "".join(ch for ch in s if ch.isalnum())
        for i in range(len(v)):
            j = -i -1
            if v[i].lower() != v[j].lower():
                return False
        return True