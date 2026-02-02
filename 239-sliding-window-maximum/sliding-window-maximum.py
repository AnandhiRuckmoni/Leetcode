import sys
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        j=0
        if len(nums) == k:
            return [max(nums)]
        l=[]
        d=deque()
        while j < len(nums):
            if len(d)==0:
                d.append(j)
            else:
                x=len(d)-1
                
                while  x >= 0 and nums[j] >= nums[d[x]]:   
                
                    del d[x]
                    x=len(d)-1
                d.append(j)
                
            if j-i+1 < k:
                j+=1
            else:
                l.append(nums[d[0]])
                if d[0]==i:
                    del d[0]
                i+=1
                j+=1
        return l