import sys
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        s1=""
        l=[]
        l1=[]
        repeating=[]
        c=0
        maxval=-sys.maxsize
        if len(s) == 0 : 
            return 0
        for i in range(len(s)):
            
            l.append(s[i])
            s1=s[i]    
            
            for j in range(i+1,len(s)):
                
                s1+=s[j]
                if len(s1) > maxval:
                    if s1 not in repeating:
                        if len([letter for letter in s1 if s1.count(letter) > 1]) > 0 :
                            repeating.append(s1)
                            break
                        if s1 not in l:
                            #print(s1,l[len(l)-1])
                            if len(s1) > len(l[len(l)-1]):
                                
                                l.append(s1)
                    else:
                        break

            if len(l) > 1000 :        
                c=len(l[len(l)-1])
                if c > maxval : 
                    maxval=c
                l.clear()
            
            else:
                c=max([len(i) for i in l])
                if c > maxval : 
                    maxval=c
        return maxval