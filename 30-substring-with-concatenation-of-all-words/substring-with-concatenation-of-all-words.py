from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d=Counter(words)
        l1=[]
        if set(words) == set(s) and len(set(s))==1:
            noofindexes=len(s)-(len(words)*len(words[0]))+1
            for i in range(noofindexes):
                l1.append(i)
            return(l1)
        i=0
        k=0
        j=i+len(words[0])
        cnt=0
        while k < len(s):
            if s[k:j] in d.keys():  
                d[s[k:j]]-=1
                if d[s[k:j]]==0:
                    del d[s[k:j]]              
                j=j+len(words[0])
                cnt+=1
                k=k+len(words[0])                
            else:
                #print(cnt)
                if cnt==len(words):                    
                    l1.append(i)
                    
                i+=1
                k=i
                j=i+len(words[0])
                cnt=0
                d=Counter(words)
            #print(i,j,k,cnt,s[k:j],len(s),d)
        if cnt==len(words):                    
            l1.append(i)
        print(l1)
        return(l1)