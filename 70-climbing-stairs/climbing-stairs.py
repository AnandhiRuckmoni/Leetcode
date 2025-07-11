d={}
class Solution:
    
    def climbStairs(self, n: int) -> int:
        x=0
        y=0
        if n < 2:
            d[n]=1
            return 1
        
        if n-1 in d.keys():
            x=d[n-1]
        else:
            x=self.climbStairs(n-1)
            d[n-1]=x
        if n-2 in d.keys():
            y=d[n-2]
        else:
            y=self.climbStairs(n-2)
            d[n-2]=y
        
        return x+y