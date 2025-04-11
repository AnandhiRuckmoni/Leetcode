class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1=""
        l=[]

        if len(s)==1:
            print(s)

        
        i=len(s)

        if s == s[::-1]:
            return s

        for j in range(len(s)):
            i=len(s)
            #print(i)
            while i >= 0 :
                d=s[j:i]
                s1=d
                i-=1
                #print(s1)
                if s1 == s1[::-1]:
                    if s1 not in l:
                        l.append(s1)
        if len(l)>0:
            c=max([len(i) for i in l])

        for i in l:
            if len(i) == c:
                s1=i
                break
            
        print(s1)
        return s1