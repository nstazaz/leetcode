class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp="".join(c for c in s if c.isalnum()).lower()
        sp=list(sp)
        print(sp) 
        spr=sp[::-1]
        print(spr)
        if sp==spr:
           return True
        else :
            return False    
        
