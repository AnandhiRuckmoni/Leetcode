class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            s=target-(nums[i])
            while j < k:
                if nums[j] + nums[k] < s:
                    l.append(nums[i]+nums[j]+nums[k])
                    j+=1
                elif nums[j]+nums[k] > s:
                    l.append(nums[i]+nums[j]+nums[k])
                    k-=1
                else:
                    l.append(target)
                    j+=1
                    k-=1
                    while (j < len(nums) and nums[j] == nums[j-1]):
                        j+=1
                    while (k>=0 and nums[k] == nums[k+1]):
                        k-=1
        
        d={abs(target-i):i for i in l}

        x=min(d.keys())
        return d[x]