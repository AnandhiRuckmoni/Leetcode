class Solution:
    def generatesubseq(self,l,start,end,ans,temp,summ):
        if summ==0 and start > end:
            ans.append(temp[:])
            return 1
        if start > end or summ<0:
            return 0
        
        
        temp.append(l[start])
        y=self.generatesubseq(l,start,end,ans,temp,summ-l[start])
        temp.remove(l[start])
        x=self.generatesubseq(l,start+1,end,ans,temp,summ)
        return x+y
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        x=self.generatesubseq(candidates,0,len(candidates)-1,ans,temp,target)
        return(ans)