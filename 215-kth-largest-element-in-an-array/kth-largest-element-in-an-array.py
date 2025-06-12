import sys
class Solution:
    def qsearch(self,a,low,high,pos):
        pivot=a[low]
        start=low
        end=high
        print("here",start,end)
        while start < end:
            while start < len(a) and a[start]<=pivot:
                start+=1
            while a[end]>pivot:
                end-=1
            if start < end:
                temp=a[start]
                a[start]=a[end]
                a[end]=temp
        temp=a[end]
        a[end]=pivot
        a[low]=temp
    
        return end
    def qsortsearch(self,a,low,high,pos):
        if low <= high:
            i=self.qsearch(a,low,high,pos)
            diff=len(a)-i
            
            if diff==pos:
               
                return i
            if diff > pos:
                return self.qsortsearch(a,i+1,high,pos)
            else:
                
                return self.qsortsearch(a,low,i-1,pos)      
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]