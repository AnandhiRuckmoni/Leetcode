class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        l=sorted(d.items(),key=lambda item:item[1],reverse=True)
        l1=[l[i][0] for i in range(k)]
        return l1