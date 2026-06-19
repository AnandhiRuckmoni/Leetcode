class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=i+k
        av=0.0
        s=sum(nums[i:j])
        av=s/k
        mx=av
        while i <=j and j < len(nums):
            s-=nums[i]
            s+=nums[j]
            i+=1
            j+=1
            av=s/k
            mx=max(mx,av)
            
        av=sum(nums[i:j])/k
        mx=max(mx,av)
        return(mx)
            