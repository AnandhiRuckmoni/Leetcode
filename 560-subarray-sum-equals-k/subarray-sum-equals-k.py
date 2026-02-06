class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """d={}
        d[0]=1
        currsum = 0
        cnt=0
        for i in range(len(nums)):
            currsum += nums[i]
            if currsum - k in d.keys():
                cnt+=d[currsum-k]
            if currsum in d.keys():
                d[currsum]+=1
            else:
                d[currsum]=1
        return cnt
"""
        i=0
        j=0
        d={}
        d[0]=1
        summ=0
        cnt=0
        
        while j < len(nums):
            summ+=nums[j]
            if summ-k in d.keys():
                cnt+=d[summ-k]
            if summ in d.keys():
                d[summ]+=1
            else:
                d[summ]=1
            j+=1
        return cnt