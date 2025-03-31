class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            l=[x for x in nums if x < target]
            if len(l)>0:
                return nums.index(max(l)) + 1
            else:
                return 0