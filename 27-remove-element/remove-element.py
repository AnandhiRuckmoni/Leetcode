class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=[x for x in nums if x != val]
        
        nums.clear()
        for x in l:
            nums.append(x)
        #print(nums)
        return len(nums)