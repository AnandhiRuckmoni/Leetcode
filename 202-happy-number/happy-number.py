class Solution:
    def findsumOfSquares(self,n)->int:
        s=0
        while n > 0:
            rem=n%10
            n//=10
            s+=rem*rem
        return s
    def isHappy(self, n: int) -> bool:
        res=n
        l=[]
        while 1==1:
            res=self.findsumOfSquares(res)
            if  res in l:
                return False
            elif res==1:
                return True
            else:
                l.append(res)
        return False
            
        