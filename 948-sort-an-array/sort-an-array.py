class Solution:
    def merge(self,a,low,mid,high):
        left=a[low:mid+1]
        right=a[mid+1:high+1]
        i=0
        j=0
        k=low
        
        while i < len(left) and j < len(right):
            if left[i]>right[j]:
                a[k]=right[j]
                k+=1
                j+=1
            else:
                a[k]=left[i]
                k+=1
                i+=1
        while i < len(left):
            a[k]=left[i]
            k+=1
            i+=1
        while j < len(right):
            a[k]=right[j]
            k+=1
            j+=1
        
        return a
    def mergeSort(self,a,low,high)->List:
        if high <=low:
            return a
        mid=(low+high)//2
        a=self.mergeSort(a,low,mid)
        a=self.mergeSort(a,mid+1,high)
        
        a=self.merge(a,low,mid,high)
        return a
    
    def sortArray(self, nums: List[int]) -> List[int]:
        l=self.mergeSort(nums,0,len(nums)-1)
        print(l)
        return l
    