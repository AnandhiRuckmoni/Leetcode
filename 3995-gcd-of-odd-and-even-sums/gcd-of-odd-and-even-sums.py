import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        l1=[]
        l2=[]
        i=1
        cnt=0
        while cnt < n:
            l1.append(i)
            l2.append(i+1)
            i+=2
            cnt+=1

        print(l1,l2)
        return math.gcd(sum(l1),sum(l2))