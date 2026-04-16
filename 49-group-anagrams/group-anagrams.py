class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d={}
        
        l1=[]
        for i in strs:
            if len(d)==0:
                d["".join(sorted(i))]=[i]
            else:
                x="".join(sorted(i))
                if x in d.keys():
                    d[x].append(i)
                else:
                    d["".join(sorted(i))]=[i]            
        for i,j in d.items():            
            l1.append(j)
        return l1