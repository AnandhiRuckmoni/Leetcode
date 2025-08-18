import numpy as np
class Solution:
    def lastRemaining(self, n: int) -> int:
        #if n%2==0 :
        #    origend=n-1
        #else:
        origend=n

        rem=n
        origstart=1
        rev=False
        step=1
        start=origstart
        end=origend
        while rem > 1:
            print(start,end,step,rev,rem)
            if not rev:
                if rem%2==0:
                    start=origend
                else:
                    start=origend-step
                end=origstart+step
            if rev:
                if rem%2==0:
                    start=origend
                else:
                    start=origend+step
                end=origstart-step
            step*=2
            rev=not rev
            rem//=2
            origstart=start
            origend=end
            
        return end
