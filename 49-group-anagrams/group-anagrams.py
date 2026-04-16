class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l=[]
        d={}
        d1={}
        l1=[]
        for i in strs:
            if len(d)==0:
                d[i]=[]
                d1["".join(sorted(i))]=i
            else:
                x="".join(sorted(i))
                #found=False
                #for j in d.keys():
                if x in d1.keys():
                    #y="".join(sorted(j))
                    #if x==y:
                    d[d1[x]].append(i)
                    #found=True
                    #break
                else:
                    d[i]=[]
                    d1["".join(sorted(i))]=i
            #print(l1)
        for i,j in d.items():
            l.append(i)
            if d[i] !=[]:
                l=l+d[i]
            l1.append(l)
            l=[]
        #print(l1)
        return l1