import heapq
class MedianFinder:

    def __init__(self):
        self.mx=[]
        self.mn=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.mx,-num)
        if self.mx and self.mn:
            largest=(self.mx[0])
            smallest=self.mn[0]
            if -largest > smallest:
                heapq.heappop(self.mx)
                heapq.heappush(self.mn,-largest)
                

        if len(self.mx)> len(self.mn):
            while len(self.mx)-len(self.mn)> 1:
                x=heapq.heappop(self.mx)
                heapq.heappush(self.mn,-x)
        if len(self.mn)>len(self.mx):
            while len(self.mn)-len(self.mx)>1:
                x=heapq.heappop(self.mn)
                heapq.heappush(self.mx,-x)
        

    def findMedian(self) -> float:
        
        if len(self.mx)==len(self.mn):
            largest=(self.mx[0])
            smallest=self.mn[0]
            return (-largest+smallest)/2
        elif len(self.mx)>len(self.mn):
            return -self.mx[0]
        else:
            return self.mn[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()