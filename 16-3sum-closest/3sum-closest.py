import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mx=sys.maxsize
        res=0
        print(mx)
        l=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            s=target-(nums[i])

            while j < k:
                summ=nums[i]+nums[j]+nums[k]
                diff=abs(target-summ)
                if diff < mx:
                    mx=diff
                    res=summ
                if nums[j] + nums[k] < s:
                    j+=1
                elif nums[j]+nums[k] > s:
                    k-=1
                else:
                    j+=1
                    k-=1
                    
        
        return res