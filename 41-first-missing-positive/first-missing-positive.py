class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=[]
        c=0
        l=[x for x in nums if x>0]
        l.sort()
        print(l)
        if len(l) > 0:
            if min(l) > 1:
                c = 1
            else:
                for i in l:
                    if i==c+1:
                        c+=1
                        continue
                c+=1
        else:
            c+=1
        return c