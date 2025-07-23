class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        t=1
        for i in order:
            d[i]=t
            t+=1
        l=[]
        x=""
        y=""
        for i in s:
            if i not in d.keys():
                y+=i
            else:
                x+=i
        z=[]
        for i in d.keys():
            z+=[j for j in x if i==j]
        res="".join(z)
        res+=y
        print(z,x)
        return res