class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums==sorted(nums) or len(nums)==1:
            return 0
        l=sorted(nums)
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
        return edidx-stidx+1
        