import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=sys.maxsize
        mxprofit=0
        for i in prices:
            minprice=min(minprice,i)
            mxprofit=max(mxprofit, i-minprice)
        print(mxprofit)
        return(mxprofit)