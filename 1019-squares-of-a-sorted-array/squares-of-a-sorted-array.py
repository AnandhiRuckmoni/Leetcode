import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #BruteForce
        #return sorted([i*i for i in nums])
        # TC = o(nlogn) 


        #optimized

        i=0
        j=len(nums)-1
        l=[]
        while i <=j:
            if abs(nums[i]) < abs(nums[j]):
                l=[nums[j] * nums[j]] +l
                j-=1
            else:
                l=[nums[i] * nums[i]] +l
                i+=1
        return l