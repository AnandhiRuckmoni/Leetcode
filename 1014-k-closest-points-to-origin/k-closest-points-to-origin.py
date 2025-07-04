import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        for i in range(len(points)):
            dist=math.sqrt(points[i][0]**2+points[i][1]**2)
            heapq.heappush(l,(-dist,points[i]))
            if i >k-1:
                heapq.heappop(l)
        l1=[]
        for i in range(k):
            x=heapq.heappop(l)
            
            l1.append((-x[0],x[1]))
        l1=sorted(l1,key=lambda x:x[0])
        print(l1)
        l=[]

        for i in l1:
            l.append(i[1])
        return l