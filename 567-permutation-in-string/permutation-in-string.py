import sys
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        flag=False
        i=0
        l=[]
        l1=[]
        while i < len(s2):
            
            if i+k<len(s2):
                x=s2[i:i+k]
                l.append(x)
            i+=1


        i=len(s2)
        while i>=0:
            if i-k>=0:
                x=s2[i-k:i]
                if x not in l:
                    l.append(x)
            i-=1
        
        for i in l:
            x=[t for t in s1 if t not in i]
            if len(x)==0:
                if sorted(i)==sorted(s1):                
                
                    flag=True
                    break
        return flag