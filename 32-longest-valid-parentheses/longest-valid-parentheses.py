import sys
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s=="":
            return 0
        l=[]
        cnt=0
        l.append(-1)
        maxi=0
        for i in range(len(s)):
            if s[i]=='(':
                l.append(i)
            if s[i]==')':
                l.pop()
                if l==[]:
                    l.append(i)
                else:
                    start=l[len(l)-1]
                    cnt=i-start
                    if cnt > maxi:
                        maxi=cnt
        return(maxi) 
            
                