from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """i=0
        j=0
        l=[]
        s1=""
        cnt=0
        k=len(p)
        c=Counter(p.lower())
        while j < len(s):
            s1+=s[j]
            if j-i+1<k:
                j+=1
            else:
                if Counter(s1.lower()) == c:
                    l.append(i)
                s1=s1[1:]
                i+=1
                j+=1
        return l"""
        t1=Counter(p)
        t2=Counter()
        print(t1,t2)
        j=0
        i=0
        l=[]
        l1=[]
        cnt=0
        while j < len(s):
            cnt+=1

            if s[j] in t2:
                t2[s[j]]+=1
            else:
                t2[s[j]]=1
            if cnt<len(p):
                j+=1
            else:
                
                if t1==t2:
                    l1.append(i)
                #print(t2,i,j,l1)
                if s[i] in t2.keys():
                    t2[s[i]]-=1
                    if t2[s[i]]==0:
                        del t2[s[i]]
                i+=1
                j+=1
                #print(i,j,t2)
        return l1
