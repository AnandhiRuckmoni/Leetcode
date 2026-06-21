class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d={i:abs(arr[i]-x) for i in range(len(arr))}
        l=sorted(d.items(),key=lambda x:(x[1],x[0]))
        l1=sorted([arr[i] for (i,j) in l[:k]])
        return(l1)