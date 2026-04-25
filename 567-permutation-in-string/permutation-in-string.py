from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=Counter(s1)
        i=0
        j=i+len(s1)-1
        while j < len(s2):
            d1=Counter(s2[i:j+1])
            if d==d1:
                return(True)
            else:
                i+=1
                j+=1
        return(False)
