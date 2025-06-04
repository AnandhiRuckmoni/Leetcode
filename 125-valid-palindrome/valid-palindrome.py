class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        l=[i if i.isalnum()==True else "" for i in s]
        
        s1="".join(l)
        if s1.lower() == s1[::-1].lower():
            return(True)
        else:
            return(False)