class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={0:[],1:[],2:[]}
        for i in range(len(arr)):
            if arr[i]==0:
                d[0].append(i)
            elif arr[i]==1:
                d[1].append(i)
            else:
                d[2].append(2)
        zerocnt=len(d[0])
        onecnt=len(d[1])
        twocnt=len(d[2])
        k=0
        for i in range(zerocnt):
            arr[k]=0
            k+=1
        for i in range(onecnt):
            arr[k]=1
            k+=1
        for i in range(twocnt):
            arr[k]=2
            k+=1