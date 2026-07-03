from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l=[]
        d=Counter(t)
        t1={}
        i=0
        j=0
        mn=sys.maxsize
        x=""
        while i <=j and j < len(s):
            word=s[i:j+1]
            if s[j] in d.keys():
                if s[j] not in t1.keys():
                    t1[s[j]]=1
                else:
                    t1[s[j]]+=1
            flag1=d.keys() == t1.keys() and all(t1[k] >= d[k] for k in d)
            while flag1:
                if j-i+1 < mn:
                    mn=j-i+1
                    x=s[i:j+1]
                if s[i] in t1.keys():
                    t1[s[i]]-=1
                    if t1[s[i]]==0:
                        del t1[s[i]]
                i+=1  
                flag1=d.keys() == t1.keys() and all(t1[k] >= d[k] for k in d)                
            if not flag1:
                j+=1
        
        return(x)