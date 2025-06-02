from functools import reduce
class Solution:

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        x=[i for i in nums if i!=0]
        if x==[]: 
            prod=0
        else:
            prod = reduce(lambda x,y: x*y,[j for j in nums if j!=0])
        if 0 in nums and nums.count(0)>1:
            prod=0
        prodwithonezero=1
        if nums.count(0)==1:
            prodwithonezero=0
        for i in nums:
            if i!=0:
                if prodwithonezero == 0:
                    l.append(0)
                else:
                    l.append(prod//i)
                
            elif prod==0:
                l.append(0)
            else:
                l.append(prod)
        return l