class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        #single occurence
        summ=0
        cnt=0
        x=0
        i=0
        while i < len(nums):
            
            if nums[i]==0:
                cnt+=1
                i+=1
            else:
                summ=(cnt*(cnt+1))//2
                x+=summ
                cnt=0
                i+=1
            
        if cnt !=0:
            summ=(cnt*(cnt+1))//2
            x+=summ
        return x