class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        d={}
        i=0
        j=0
        cnt=0
        while i <=j and j < len(nums):
            if nums[j] in d.keys():
                d[nums[j]]+=1
                j+=1
            else:
                if len(d) < 2:
                    d[nums[j]]=1
                    j+=1
                else:
                    cnt=max(cnt,j-i)
                    while len(d) >=2:
                        d[nums[i]]-=1
                        if d[nums[i]]==0:
                            del d[nums[i]]
                        i+=1
                    d[nums[j]]=1
                    j+=1
        cnt=max(cnt,j-i)
        return(cnt)