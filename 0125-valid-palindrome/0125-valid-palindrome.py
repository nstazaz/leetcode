class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp=list()
        for c in s:
            if c.isalnum():
                sp.append(c.lower())
                #print(sp)
        t=len(sp)
        for x in range(t):
            if sp[x]!=sp[t-1-x] :
                return False
        return True         