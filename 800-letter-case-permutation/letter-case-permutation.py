class Solution:
    def permutations(self,l,ans,temp,idx,res):
        if idx==len(l):
            if ans not in res:
                res.append(ans)
            return
        
        if idx not in temp:
            temp.append(idx)
            self.permutations(l,ans+l[idx],temp,idx+1,res)
            temp.pop()
            self.permutations(l,ans+l[idx].swapcase(),temp,idx+1,res)
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=""
        temp=[]
        res=[]
        self.permutations(s,ans,temp,0,res)
        return res