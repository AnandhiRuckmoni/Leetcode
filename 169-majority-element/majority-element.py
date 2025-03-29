class Solution:
    def majorityElement(self, nums: list) -> int:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        return (max(d,key=d.get))
        