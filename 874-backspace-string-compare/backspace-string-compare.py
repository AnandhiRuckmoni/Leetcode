class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=0
        j=i+1
        l=[]
        while i < len(s):
            if s[i] !='#':
                l.append(s[i])
                i+=1
            else:
                if len(l)>0:
                    l.pop()
                i+=1
        res="".join(l)
        l=[]
        i=0
        print(res)
        while i < len(t):
            if t[i] !='#':
                l.append(t[i])
                i+=1
            else:
                if len(l)>0:
                    l.pop()
                i+=1
        res1="".join(l)
        print(res1)
        return (res==res1)