from collections import Counter
import sys
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        mxlen=-sys.maxsize
        i=0
        j=0
        while j < len(fruits):
            if len(d) < 2:
                if fruits[j] in d.keys():
                    d[fruits[j]]+=1
                else:
                    d[fruits[j]]=1
                j+=1
            elif len(d)==2:
                if fruits[j] in d.keys():
                    d[fruits[j]]+=1
                    j+=1
                else:
                    cnt=sum(d.values())
                    mxlen=max(mxlen,cnt)
                    while len(d)==2:
                        d[fruits[i]]-=1
                        
                        
                        if d[fruits[i]]==0:
                            del d[fruits[i]]
                        i+=1
                    #i+=1
        if len(d)>0:
            cnt=sum(d.values())
            mxlen=max(mxlen,cnt)
        
        return(mxlen)
                    