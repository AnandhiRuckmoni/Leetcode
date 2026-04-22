from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        if len(t) > len(s):
            return ""
        l=Counter(t)
        compare_len=len(t)
        l1=[]
        i=0
        j=0
        min_len=sys.maxsize
        while j < len(s):            
            if l[s[j]]>0:
                compare_len-=1
            l[s[j]]-=1
            j+=1
            while compare_len==0:
                #l1.append(s[i:j])
                #l=Counter(t)
                if j-i < min_len:
                    min_len=j-i
                    start=i
                l[s[i]]+=1
                if l[s[i]] > 0:
                    compare_len+=1
                i+=1
        if min_len==sys.maxsize:
            return ""
        
        
        return(s[start:start+min_len])
        