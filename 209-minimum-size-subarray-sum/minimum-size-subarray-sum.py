import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        mn=sys.maxsize
        i=0
        j=i+1
        if nums[i] >=target:
            return 1
        elif nums[j] >=target:
            return 1
        s=sum(nums[i:j+1])
        print(i,j,s,mn)
        while i < len(nums) and j < len(nums):
            if s < target:
                j+=1
                if j < len(nums):
                    s+=nums[j]
            else:
                mn=min(mn,j-i+1)
                s-=nums[i]
                i+=1
                #mn=min(mn,j-i+1)
            print(i,j,s,mn)
        #print(mn)
        return(mn)