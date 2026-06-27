from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l=[]
        t=Counter(s)
        d=Counter(words)
        print(len(Counter(s)),len(t))
        
        #print(t)
        wordlength=len(words[0])
        print(d,t)
        if len(d)==len(t) and len(d.keys())==1 and len(t.keys())==1 and list(d.keys())[0]==list(t.keys())[0]:
            print('hi')
            l=[i for i in range(0,len(s)-(len(words)*wordlength)+1)]
            return(l)
        i=0
        j=i+wordlength
        while i <=j and j <= len(s):
            #print(i,j,d)
            word=s[i:j]
            if word in d.keys():
                d[word]-=1
                if d[word]==0:
                    del d[word]
                if d=={}:
                    k=(len(words)-1) *wordlength
                    idx=i-k
                    #print(k,idx)                    
                    l.append(idx)
                    d=Counter(words)
                    i=idx+1
                    j=i+wordlength
                else:
                    i+=wordlength
                    j=i+wordlength
            else:
                if d!={}:
                    k=(len(words)-sum(d.values()))*wordlength
                    
                    i=i-k+1
                    j=i+wordlength
                    #print(k,i,j)
                    d=Counter(words)
                else:
                    i+=1
                    j+=1
                    
        #print(l)
        return(l)