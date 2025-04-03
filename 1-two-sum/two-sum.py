class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        #print(d)
        l=[]
        for i in range(len(nums)):
            
            c=target-nums[i]
            if c in d.keys():
                if d[c] != i :
                    if i not in l:
                        l.append(i)
                    if d[c] not in l:
                        l.append(d[c])
            #print(sorted(l))
        return sorted(l)