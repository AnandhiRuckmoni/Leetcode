class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}

        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        print(d)
        tot=0
        for i,j in d.items():
            if j > 2:
                print(i,j,tot)
                nums[tot]=i
                nums[tot+1]=i
                tot+=2
            else:
                print(i,j,tot)
                idx=tot
                for k in range(j):
                    
                    nums[idx]=i
                    idx+=1                    
                tot+=j
                
        print(tot)
        return(tot)