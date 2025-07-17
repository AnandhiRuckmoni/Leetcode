class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1=[]
        i=0
        while i <k:
            x=nums.pop()
            nums.insert(0,x)
            i+=1