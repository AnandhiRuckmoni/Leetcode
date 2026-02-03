class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=0
        summ=0
        mx=-sys.maxsize
        while j < len(nums):
            summ+=nums[j]
            if j-i+1<k:
                j+=1
            else:
                mx=max(mx,summ)
                summ-=nums[i]
                i+=1
                j+=1
        return mx/k