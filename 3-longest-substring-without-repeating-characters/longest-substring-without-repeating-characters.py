from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=i+1
        if len(Counter(s))==1:
            return 1
        mx=0
        while i <= j and j < len(s):
            s1=s[i:j]
            #print(i,j,s1)
            t=Counter(s1)
            while max(t.values())==1 and j <= len(s):
                #print(t,i,j)
                mx=max(mx,j-i)
                j+=1
                s1=s[i:j]
                t=Counter(s1)
            i+=1
            #j+=1
        return(mx)
        
