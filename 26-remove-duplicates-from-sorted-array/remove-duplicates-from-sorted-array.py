import sys
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        dups=[]
        unique=[]
        x=-sys.maxsize
        while i < j:
            if nums[i] !=nums[j]:
                if nums[i] not in unique:
                    unique.append(nums[i])
                else:
                    dups.append(i)
                if nums[j] not in unique:
                    unique.append(nums[j])
                else:
                    dups.append(j)
            else:
                if nums[i] not in unique:
                    unique.append(nums[i])
                    dups.append(j)
                else:
                    dups.append(i)
                    dups.append(j)
            i+=1
            j-=1
        if i ==j:
            if nums[i] not in unique:
                unique.append(nums[i])
            else:
                dups.append(i)
        print(i,j,dups,unique)
        for i in dups:
            nums.append(nums[i])
            nums[i] = x
        i=0
        for i in nums[:]:
            if i==x:
                nums.remove(i)
        
        return len(unique)