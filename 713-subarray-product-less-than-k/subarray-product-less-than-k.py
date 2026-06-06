import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==0:
            return 0
        if math.prod(nums) < k:
            return (n*(n+1)//2)
        i=0
        j=i
        cnt=0
        p=math.prod(nums[i:j+1])
        while i < n:            
            #print(i,j,p,cnt)
            if  p< k:
                cnt+=1
                j+=1
                if j < n:
                    p*=nums[j]
            else:
                p//=nums[i]
                i+=1
                temp=math.prod(nums[i+1:j+1])
                p//=temp
                j=i
                if j < n:
                    p=nums[i]
                #print(i,j,p,cnt)
                
            if i<n and j >=n:
                p/=nums[i]
                i+=1
                temp=math.prod(nums[i+1:j+1])
                p//=temp     
                j=i
        return(cnt)