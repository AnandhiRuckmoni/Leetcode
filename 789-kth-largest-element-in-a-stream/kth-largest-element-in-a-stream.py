import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums       
        self.k=k
        heapq.heapify(self.nums)
    def findkthlargest(self):
        l=self.nums[:]
        l1=[]
        #print(l,self.nums)
        for i in range(len(self.nums)-self.k+1):
            x=heapq.heappop(l)
            #print(x)
        #print(x)
        return x

    def add(self, val: int) -> int:
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        heapq.heappush(self.nums,val)
        x=self.findkthlargest()
        return x
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)