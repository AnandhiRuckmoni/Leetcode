from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i=0
        j=i+k
        flag=1 if k%2!=0 else 0
        l=SortedList(nums[i:j])
        l1=[]
        while i < j and j < len(nums):
            if flag==1:
                mid=k//2
                l1.append(l[mid])
            else:
                mid=k//2
                l1.append((l[mid]+l[mid-1])/2)
            l.remove(nums[i])
            i+=1
            l.add(nums[j])
            j+=1
        if flag==1:
            mid=k//2
            l1.append(l[mid])
        else:
            mid=k//2
            l1.append((l[mid]+l[mid-1])/2)
        print(l1)
        return(l1)