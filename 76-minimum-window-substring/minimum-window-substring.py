from collections import Counter
import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i=0
        j=0
        d=Counter(t)
        clen=len(t)
        min_len=sys.maxsize
        while j < len(s):
            if d[s[j]]>0:
                clen-=1
            d[s[j]]-=1
            j+=1
            while clen ==0:
                if j-i < min_len:
                    min_len=j-i
                    start=i
                d[s[i]]+=1
                if d[s[i]] > 0:
                    clen+=1
                i+=1
        if min_len==sys.maxsize:
            return ""
        else:
            return s[start:start+min_len]