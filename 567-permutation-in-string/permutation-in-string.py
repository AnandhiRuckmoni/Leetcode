from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=Counter(s1)
        searchLength=len(s1)
        i=0
        j=i+searchLength
        while i <=j and j <= len(s2):
            word=s2[i:j]
            d1=Counter(word)
            if d==d1:
                return True
            else:
                i+=1
                j+=1
        return False