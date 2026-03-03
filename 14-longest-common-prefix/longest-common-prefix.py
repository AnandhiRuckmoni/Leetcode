class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[]
        l=sorted(strs,key=len)
        res=l[0]
        
        for i in l[1:]:
            for j in range(len(res)):
                #print(i,res,res[j])
                if i.startswith(res[:j+1]):
                    continue
                else:
                    res=res[:j]
                    break
        return res
        