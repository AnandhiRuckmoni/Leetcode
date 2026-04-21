class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx=0
        cnt=0
        i=0
        j=0
        while j < len(nums):
            if nums[j]==1:
                cnt+=1
                j+=1
            else:
                mx=max(mx,cnt)
                j+=1
                i=j
                cnt=0
        
        mx=max(mx,cnt)
        return mx