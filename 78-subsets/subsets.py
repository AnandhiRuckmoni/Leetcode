class Solution:
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def helper(nums,low,op):
            if low == len(nums):
                l.append(op[:])
                return
            op.append(nums[low])
            helper(nums,low+1,op)
            op.pop()
            helper(nums,low+1,op)
        helper(nums,0,[])
        print(l)
        return l