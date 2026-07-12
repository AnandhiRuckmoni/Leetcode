class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while 1==1:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
            if slow==fast:
                slow=0
                while slow!=fast:
                    slow=nums[slow]
                    fast=nums[fast]
                break        
        return slow
        