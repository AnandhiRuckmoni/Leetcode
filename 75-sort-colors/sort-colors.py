class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        index=0
        d={i:nums.count(i) for i in nums}
        nums.clear()
        for i in range(0,3):
            if i in d.keys():
                val=d[i]
                while d[i] > 0:
                    nums.insert(index,i)
                    d[i]-=1
                    index+=1
        return(nums)