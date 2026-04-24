from collections import Counter
import sys
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # How to flip anyting other than A to A at the most k times to get the longest consecutive As
        cnt=0
        mxlen=-sys.maxsize
        l1=[]
        if k==0:
            for i in s:
                print(i,l1)
                if i not in l1 and l1==[]:
                    l1.append(i)
                elif i not in l1 and l1!=[]:
                    mxlen=max(len(l1),mxlen)
                    l1=[]
                    l1.append(i)
                elif i in l1:
                    l1.append(i)
                print(mxlen)
            if  mxlen==-sys.maxsize or l1!=[]:
                mxlen=max(len(l1),mxlen)
            print(mxlen)
            return(mxlen)
        else:
            cnt=0
            mxlen=-sys.maxsize
            i=0
            j=0
            d={}
            while j < len(s):                
                if s[j] in d.keys():
                    d[s[j]]+=1
                else:
                    d[s[j]]=1
                windowsize=j-i+1
                max_freq = max(d.values())
                noofreplacements=windowsize-max_freq
                #print(i,j,d,noofreplacements)
                if noofreplacements <= k:
                    j+=1
                else:
                    mxlen=max(j-i,mxlen)
                    while noofreplacements > k:
                        d[s[i]]-=1
                        if d[s[i]]==0:
                            del d[s[i]]
                        i+=1
                        windowsize=j-i+1
                        max_freq = max(d.values())
                        noofreplacements=windowsize-max_freq
                    j+=1
            mxlen=max(j-i,mxlen)
            #print(mxlen)
            return(mxlen)
