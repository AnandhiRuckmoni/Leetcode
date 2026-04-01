class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tgt=-1*nums[i]
            j=i+1
            k=len(nums)-1
            #print(i,j,k)
            while j < k:
                    
                if nums[j] + nums[k] < tgt:
                    j+=1
                elif nums[j] + nums[k] > tgt:
                    k-=1
                else:
                    #print (i,j,k)
                    #if [nums[j],nums[k],-1*tgt] not in l:
                    l.append([nums[j],nums[k],-1*tgt])
                    j+=1
                    k-=1
                    while j< len(nums) and nums[j]==nums[j-1]:
                        j+=1
                    while k>=0 and nums[k]==nums[k+1]:
                        k-=1
        l1=[]
        l1=[i for i in l if i not in l1]
        return l1