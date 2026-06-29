from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        d=deque()
        if sorted(nums,reverse=True)==nums:
            i=0
            j=i+k
            while i < j and j <= len(nums):
                l.append(nums[i])
                i+=1
                j+=1
            return(l)
        
        i=0
        j=i+k

        
        
        for t in range(i,j):            
            while d and nums[t] > nums[d[-1]]:
                d.pop()
            d.append(t)
        l.append(nums[d[0]])
        i+=1
        j+=1
        while i < j and j <= len(nums):      
            while d and d[0] < i:
                d.popleft()
            while d and nums[j-1] > nums[d[-1]]:
                d.pop()
            d.append(j-1)
            l.append(nums[d[0]])
            i+=1
            j+=1
            
        return(l)