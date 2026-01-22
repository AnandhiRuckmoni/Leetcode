class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l1=set()
        nums.sort()
        i=0
        j=i+1
        k=len(nums)-1
        while i < j < k:            
            target= 0-nums[i]
            while j < k:
                if nums[j]+nums[k]==target:
                    
                    l1.add((nums[i],nums[j],nums[k]))
                    
                    j+=1
                    k-=1
                elif nums[j]+nums[k]< target:
                    j+=1
                else:
                    k-=1
            i+=1
            j=i+1
            k=len(nums)-1
        
        return [list(item) for item in l1]