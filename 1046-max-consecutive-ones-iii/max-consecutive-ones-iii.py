import sys
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt=0
        mxlen=-sys.maxsize
        if k==0:
            for i in nums:
                if i ==1:
                    cnt+=1
                else:
                    mxlen=max(cnt,mxlen)
                    cnt=0
                mxlen=max(cnt,mxlen)
            return mxlen
        else:
            cnt=0
            mxlen=-sys.maxsize
            i=0
            j=0
            while j < len(nums):
                print(i,j,cnt)
                if nums[j]==1:
                    j+=1
                else:
                    if cnt <= k:
                        cnt+=1                        
                    if cnt > k:                        
                        mxlen=max(j-i,mxlen)
                        while cnt > k:                            
                            if nums[i]==0:
                                cnt-=1
                            i+=1                        
                    j+=1
                print(mxlen)
            mxlen=max(j-i,mxlen)
            return(mxlen)


        