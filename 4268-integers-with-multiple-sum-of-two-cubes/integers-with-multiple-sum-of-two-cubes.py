import math
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        d={}
        l1=[]
        mx=int(math.cbrt(n))
        i=1
        j=mx
        while i <= j:
            x=i**3+j**3
            #print(i,j,x,l,l1)
            if x > n:
                j-=1
                continue
            else:
                k=i+1
                if x in d.keys():
                    l1.append(x)
                else:
                    d[x]=1
                while k< j:
                    y=i**3 + k**3
                    #print(i,j,x,y,l,l1,y in l)
                    if y in d.keys() and y not in l1:
                        l1.append(y)
                    else:
                        d[y]=1
                    k+=1
            
            i+=1
        print(len(l1))
        return sorted(l1)