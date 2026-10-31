class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp="".join(c for c in s if c.isalnum()).lower()
        sp=list(sp)
        print(sp) 
        spr=sp[::-1]
        print(spr)
        t=len(sp)
        for x in range(t):
            if sp[x]!=spr[x]:
                return False
        return True         