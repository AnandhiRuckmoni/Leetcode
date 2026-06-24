class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt=len([i for i in nums if i < k])
        if prod(nums)<k:
            return (len(nums) * (len(nums)+1))//2
        i=0
        j=1
        d={}
        while i<j and j<len(nums): 
            p=prod(nums[i:j+1])           
            print(j,d,cnt,p)
            if p<k :
                cnt+=1
                j+=1                
            else:
                p=p//nums[i]
                i+=1
                j=i+1
            if j > len(nums)-1:
                p=p//nums[i]                
                i+=1
                j=i+1 
        #print(cnt)
        return(cnt)