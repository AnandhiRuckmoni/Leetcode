class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        if j >=2:
            while i <j:
                if nums[i]<nums[i+1] and nums[i+1] > nums[i+2]:
                    return(i+1)
                    break
                else:
                    i+=1
                if nums[j]<nums[j-1] and nums[j-1]>nums[j-2]:
                    return(j-1)
                    break
                else:
                    j-=1
        else:
            return nums.index(max(nums))
        return nums.index(max(nums))