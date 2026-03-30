import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        

        #BruteForce
        #return sorted([i*i for i in nums])
        # TC = o(nlogn) 

#-------------------------------------------------------------------------
        #optimized

        """   i=0
        j=len(nums)-1
        l=[]
        while i <=j:
            if abs(nums[i]) < abs(nums[j]):
                l=[nums[j] * nums[j]] +l
                j-=1
            else:
                l=[nums[i] * nums[i]] +l
                i+=1
        return l"""

#-------------------------------------------------------------------------
        pos=[i for i in nums if i>=0]
        neg=[i for i in nums if i < 0]
        pos=[i*i for i in pos]
        neg=[i*i for i in neg]
        neg=neg[::-1]
        i=0
        j=0
        
        l=[]
        print(pos,neg)
        while i < len(neg) and j < len(pos):
            if neg[i] <= pos[j]:
                l.append(neg[i])
                i+=1
            else:
                l.append(pos[j])
                j+=1
        while i < len(neg):
            l.append(neg[i])
            i+=1
        while j < len(pos):
            l.append(pos[j])
            j+=1
        return l