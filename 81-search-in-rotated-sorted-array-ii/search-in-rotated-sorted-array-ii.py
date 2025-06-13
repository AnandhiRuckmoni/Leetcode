class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=nums
        x=-1
        while l!=sorted(nums):
            x=l.pop(-1)
            l.insert(0,x)
        low=0
        high=len(l)-1
        print(l)
        x=-1
        while low <=high:
            mid=(low+high)//2
            if l[mid]==target:
                x=mid
                break
            elif l[mid] < target:
                low=mid+1
            elif l[mid] > target:
                high=mid-1
        print(x)
        if x!=-1:
            return True
        else:
            return False