class Solution:
    def permutation(self,l,ans,l1):
        if len(l1)==len(l):
            ans.append([i for i in l1])
            return
        
        
        for i in range(len(l)):
            print('return value',l1,i)
            if l[i] not in l1:
                l1.append(l[i])
                print(l1, i,'bef')
                self.permutation(l,ans,l1)
                print(l1, i,'aft')
                l1.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l1=[]
        self.permutation(nums,ans,l1)
        return ans

        