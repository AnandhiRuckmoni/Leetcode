import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        d={}
        l=[]
        l=list(set(nums))
        
        if len(l)==1 and math.prod(nums)<k:
            x=len(nums)
            return (x*(x+1))//2
        #nums.sort()
        
        i=0
        j=i+1
        while i <len(nums):
            #print(i,j)
            if  nums[i] < k and (i) not in d.keys():
                d[(i)]=1
            
            if  nums[j] < k and (j) not in d.keys():
                d[(j)]=1
            x=math.prod(nums[i:j+1])
            t=(i) if i==j else tuple(range(i,j+1))
            #print(i,j,x,tuple(range(i,j+1)),t)
            
            if x < k and t not in d.keys():
                d[t]=1
                j+=1
                if j> len(nums)-1 :                
                    i+=1
                    if i >= len(nums)-1:
                        j=i
                    else:
                        j=i+1
            else:
                i+=1
                if i >= len(nums)-1:
                    j=i
                else:
                    j=i+1
        #print(nums,d.keys())
        return(len(d))