class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        print(nums)

        l=[]
        cnt=0
        for i in range(len(nums)-1):
            l.append(nums[i+1]-nums[i])
        print(l)
        cnt=0
        l1=[]
        for i in l:
            if i==0 or i==1:
                if i==1:
                    cnt+=1
            else:
                l1.append(cnt)
                cnt=0
        l1.append(cnt)
        x=max(l1)+1
        return x