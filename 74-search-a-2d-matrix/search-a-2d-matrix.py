class Solution:
    def bs(self,a,target):
        low=0
        high=len(a)-1
        while low <= high:
            mid=(low+high)//2
            
            if target > a[mid]:
                low=mid+1
            elif target < a[mid]:
                high=mid-1
            else:
                return mid
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x=-1
        for i in matrix:
            lastelementinrow=i[len(i)-1]
            
            if target <= lastelementinrow:
                
                x=self.bs(i,target)
                
                break
        if x!=-1:
            return True
        else:
            return False