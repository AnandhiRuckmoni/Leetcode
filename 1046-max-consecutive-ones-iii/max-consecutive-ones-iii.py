class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mx=-1        
        i=0
        j=0
        cnt=0
        if k==0:
            for i in nums:
                if i ==1:
                    cnt+=1
                else:
                    mx=max(cnt,mx)
                    cnt=0
            
            mx=max(cnt,mx)
            return(mx)
        while i <=j and j < len(nums):
            if nums[j]==1:
                j+=1
            else:
                if cnt < k:
                    cnt+=1
                    j+=1
                else:
                    mx=max(j-i,mx)
                    #print(i,j,mx)
                    while cnt==k:
                        if nums[i]==1:
                            i+=1
                        else:
                            cnt-=1
                            i+=1
                    
        
        mx=max(j-i,mx)
        return(mx)