class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i=0
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
        return l