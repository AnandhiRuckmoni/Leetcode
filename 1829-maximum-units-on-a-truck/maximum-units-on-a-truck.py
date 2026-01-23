class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        cnt=0
        boxTypes.sort(key=lambda x:x[1],reverse=True)

        for i in boxTypes:
            if i[0] < truckSize:
                cnt+=i[0]*i[1]
            else:
                cnt+=truckSize * i[1]
            truckSize -=i[0]
            if truckSize <= 0:
                break
        return(cnt)