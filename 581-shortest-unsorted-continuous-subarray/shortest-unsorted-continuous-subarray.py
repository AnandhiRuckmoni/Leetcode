import sys
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums==sorted(nums) or len(nums)==1:
            return 0
        #Copy the array to another array, sort and compare the indices for missorted order - o(nlogn)    
        """l=sorted(nums)
        i=0
        stidx=-1
        edidx=-1
        for i in range(len(l)):
            if l[i]!=nums[i]:                
                if stidx==-1:
                    stidx=i
                    break
        

        i=len(l)-1
        while i >=0:
            if l[i]!=nums[i]:
                if edidx==-1:
                    edidx=i
                    break
            i-=1
        return edidx-stidx+1"""
        #traverse the array keeping track of max as you go from L->R and min as you go from R->L, when there is missorted order keep updating the idx for start and end.O(n) complexity.
        i=0
        j=len(nums)-1
        mx=-sys.maxsize
        mn=sys.maxsize
        stidx=-1
        edidx=-1
        while i < len(nums) or j >=0:
            if i < len(nums):
                mx=max(mx,nums[i])
                if nums[i] < mx:
                    print(i,mx)
                    stidx=i
                i+=1
            if j >=0:
                mn=min(mn,nums[j])
                if nums[j]>mn:
                    print(j,mn)
                    edidx=j
                j-=1
        print(stidx,edidx)
        return stidx-edidx+1