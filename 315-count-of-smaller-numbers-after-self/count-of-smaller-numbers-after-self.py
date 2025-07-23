class Solution:
    def merge(self,l,start,mid,end,d):
        i=start
        j=mid+1
        l1=[]
        while i <= mid and j <=end:
            x=l[i]
            y=l[j]
            s1=x.split('/')
            s2=y.split('/')
            if int(s1[0]) > int(s2[0]):
                l1.append(x)
                d[x]+=(end-j+1)
                i+=1
            else:
                l1.append(y)
                j+=1
        while i <=mid:
            l1.append(l[i])
            i+=1
        while j <=end:
            l1.append(l[j])
            j+=1
        k=start
        for i in l1:
            l[k]=i
            k+=1
    def msort(self,l,start,end,d):
        mid=(start+end)//2
        if start>=end:
            return
        self.msort(l,start,mid,d)
        self.msort(l,mid+1,end,d)
        self.merge(l,start,mid,end,d)
        return    
    def countSmaller(self, nums: List[int]) -> List[int]:
        l1=[]
        l=[str(nums[i])+'/'+str(i) for i in range(len(nums))]
        d={str(nums[i])+'/'+str(i) :0 for i in range(len(nums))}
        self.msort(l,0,len(l)-1,d)
        for i,j in d.items():
            l1.append(j)
        print(l,d)
        return l1