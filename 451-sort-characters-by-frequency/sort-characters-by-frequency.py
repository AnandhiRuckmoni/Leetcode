class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        l=[]
        l=[i[0] for i in (sorted(d.items(),key=lambda x:(-x[1], x[0])))]
        s1=""
        for i in l:
            s1+=i*d[i]
        return s1