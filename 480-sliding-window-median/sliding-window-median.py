from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i=0
        j=i+k
        mid=k//2
        l1=[]
        flag=(1 if k%2 !=0 else 0)       
        l=SortedList(nums[i:j])
        
        for i in range(k, len(nums)):                       
            #print(i,mid,l)
            if flag==1:
                l1.append(l[mid])
            else:
                l1.append((l[mid]+l[mid-1])/2)
            l.remove(nums[i-k])
            l.add(nums[i])
        if flag==1:
            l1.append(l[mid])
        else:
            l1.append((l[mid]+l[mid-1])/2)
        return(l1)