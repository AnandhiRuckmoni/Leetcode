from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        l=[]
        d=Counter(words)
        wordlength=len(words[0])
        noofwords=len(words)
        totalstrlength=noofwords*wordlength
        #print(len(s),totalstrlength,d)
        if wordlength==1 and len(d)==1:
            if len(Counter(s))==1:
                if s[0]==words[0]:
                    t=len(s)-list(d.values())[0]
                    for i in range(t+1):
                        l.append(i)
                    return(l)
            
        
        
        i=0
        j=i+wordlength
        s1=""
        cnt=0
        flag=False
        while i <=j and j <= len(s):
            s1=s[i:j]
            
            if cnt==0 and not flag:
                idx=i
                flag=True
            if s1 in d.keys():
                d[s1]-=1
                if d[s1]==0:
                    del d[s1]
                cnt+=1
                i+=wordlength
                j+=wordlength
            else:
                d=Counter(words)
                i=idx+1
                j=i+wordlength
                cnt=0
                flag=False
            #print(i,j,s1,d,cnt,l)
            if cnt==noofwords and d=={}:
                l.append(idx)
                d=Counter(words)
                cnt=0
                flag=False
                i=idx+1
                j=i+wordlength
        if cnt==noofwords and d=={}:
            l.append(idx)
        return(l)