class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp="".join(c for c in s if c.isalnum()).lower()
        sp=list(sp)
        t=len(sp)
        for x in range(t):
            if sp[x]!=sp[t-1-x] :
                return False
        return True         