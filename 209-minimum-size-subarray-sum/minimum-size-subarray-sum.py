import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if len(nums)==1:
            return 1        
        i=0
        j=i+1
        s=nums[i]
        mn=sys.maxsize
        if s >=target:
            mn=1
        while i <=j and j < len(nums):
            s+= nums[j]
            while s >=target:
                mn=min(mn,j-i+1)
                s-=nums[i]
                i+=1
            
            j+=1
        if s >=target:
            mn=min(mn,j-i+1)
        
        return(mn)