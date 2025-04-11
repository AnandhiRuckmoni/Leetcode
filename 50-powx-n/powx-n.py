import decimal
class Solution:
    def myPow(self, x: float, n: int) -> float:
        x=decimal.Decimal(x)
        if abs(x)==decimal.Decimal(1) :
            if x < 0 and n %2 == 0 :
                return abs(x)
            if x < 0 and n % 2 !=0 :
                return x
            else:
                return x
        if n < 0:
            x=1/x
            n=-n

        if n == 0 :
            return float(1)
        
        prod=decimal.Decimal(x)
        for i in range(1,n):
            prod*=x
            if prod==decimal.Decimal('0E-10'):
                break
        return prod