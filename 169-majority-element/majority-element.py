import sys
class Solution:
    def majorityElement(self, nums: list) -> int:
        d={}
        m=-sys.maxsize
        n=0
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        
        for i,j in d.items():
            if j > m:
                m=j
                n=i
        
        return n