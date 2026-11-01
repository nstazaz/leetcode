class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp=[c.lower() for c in s if c.isalnum()]
        t=len(sp)
        for x in range(t):
            if sp[x]!=sp[t-1-x] :
                return False
        return True         