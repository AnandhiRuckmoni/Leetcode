class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited=[]
        l=[]
        for i in range(len(nums)):
            while i < len(nums):
                if i not in visited:
                    l.append(i)
                    visited.append(i)
                    nextidx=(i+nums[i])%len(nums)
                    if nextidx in l:
                        loc=l.index(nextidx)
                        
                        lpos=[1 for j in l[loc:] if nums[j] > 0]
                        lneg=[1 for j in l[loc:] if nums[j] < 0]
                        #print(loc,l[loc:],lpos,lneg)
                        if len(lpos) == len(l[loc:]) or len(lneg)==len(l[loc:]):
                            if len(l[loc:]) > 1:
                                #print('True',lpos,lneg)
                                return True
                    i=nextidx
                else:
                    l=[]
                    break
        return False