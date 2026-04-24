from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l1=[]
        d1=Counter(p)
        i=0
        j=i+len(p)-1
        
        while j < len(s):
            d2=Counter(s[i:j+1])
            if d1==d2:
                l1.append(i)
            i+=1
            j+=1
        print(l1)
        return(l1)