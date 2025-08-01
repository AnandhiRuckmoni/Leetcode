class Solution:
    def permutation(self,l,ans,l1):        
        l2=[]
        if len(l1)==len(l):
            l2=[l[i] for i in l1]
            if l2 not in ans:
                ans.append(l2)
            return
        for i in range(len(l)):            
            if i not in l1:
                l1.append(i)
                self.permutation(l,ans,l1)                              
                l1.pop()
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l1=[]
        self.permutation(nums,ans,l1)
        return ans