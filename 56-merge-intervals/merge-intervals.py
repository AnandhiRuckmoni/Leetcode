import sys
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=[]
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        #print(intervals)
        start=intervals[0][0]
        end=intervals[0][1]
        unmerged=[]
        for i in range(1,len(intervals)):
            if (start<=intervals[i][0]<= end) or (start<=intervals[i][1]<= end):
                start=min(start,intervals[i][0])
                end=max(end,intervals[i][1])
            else:
                l.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        print(start,end,unmerged)
        l.append([start,end])
        l+=[intervals[i] for i in unmerged]
        return l