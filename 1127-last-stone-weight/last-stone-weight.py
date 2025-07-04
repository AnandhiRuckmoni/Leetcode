import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l=[]
        for i in range(len(stones)):
            heapq.heappush(l,-stones[i])
        print(l)
        if len(l)==2 and l[0] == l[1]:
            return 0
        while len(l)>1:
            x=-heapq.heappop(l)
            y=-heapq.heappop(l)
            print(x,y)
            if x!=y:
                if x<y:
                    y=y-x
                    heapq.heappush(l,-y)
                else:
                    x=x-y
                    heapq.heappush(l,-x)
            elif x==y:
                heapq.heappush(l,0)
        return -l[0]