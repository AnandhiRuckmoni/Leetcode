import sys
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        start = 0
        cnt=0
        l=[]
        if s=="":
            return 0
        l.append(s[start])
        start +=1
        
        while start <len(s):
            if l!=[]: 
                if s[start] not in l:
                    l.append(s[start])
                else:
                    
                    indx=l.index(s[start])
                    
                    if cnt < len(l):
                        cnt=len(l)
                        
                    
                    val=start-len(l)+indx+1
                    #print(l,start,indx,val)
                    l.clear()
                    l=list(s[val:start])
                    
                    l.append(s[start])
                    #print(l)
                    
            else:
                l.append(s[start])
            start +=1
        if l!=[]:
            if cnt < len(l):
                cnt=len(l)
        return cnt