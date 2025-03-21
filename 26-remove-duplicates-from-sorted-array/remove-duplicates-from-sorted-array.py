class Solution:
        def removeDuplicates(self, nums: list) -> int:
            d={}
            for i in nums:
                d[i]=1
            print(d)
            nums.clear()
            for i in d.keys():
                nums.append(i)
            return len(nums)       
                    