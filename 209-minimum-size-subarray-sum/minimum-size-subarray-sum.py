import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        mn=sys.maxsize
        i=0
        j=0
        if nums[i] >=target:
            return 1
        s=0
        while i < len(nums) and j < len(nums):
            s+=nums[j]
            while s >= target:
                mn=min(mn,j-i+1)
                s-=nums[i]
                i+=1
            j+=1
            
        return(mn)