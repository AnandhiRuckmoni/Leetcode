class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={nums[i]:i for i in range(len(nums))}
        i=0
        while i < len(nums):
            if target-nums[i] in d.keys() and i!=d[target-nums[i]]:
                return [i,d[target-nums[i]]]
            i+=1