class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l=[]
        nums.sort()
        
        for i in range(0,len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tgt=target-nums[i]
            for j in range(i+1,len(nums)-2):                
                #if j > 1 and  nums[j] == nums[j-1]:
                    #continue
                left=j+1
                right=len(nums)-1
                
                while left < right:
                    #print(j,left,right)
                    s=nums[j]+nums[left]+nums[right]
                    if s==tgt:
                        if [nums[i],nums[j],nums[left],nums[right]] not in l:
                            l.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif s> tgt:
                        right-=1
                    else:
                        left+=1
        return(l)