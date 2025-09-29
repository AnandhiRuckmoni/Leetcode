class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return 
        
        if m ==0:
            nums1.clear()
            for i in nums2:
                nums1.append(i)
            return
        
        i=m
        j=0

        while i < m+n:
            nums1[i] = nums2[j]
            j+=1
            i+=1
        nums1.sort()