import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=[]
        for i in range(len(nums)):
            heapq.heappush(l,nums[i])
            if i > k-1:
                x=heapq.heappop(l)
                print(x)
        return l[0]