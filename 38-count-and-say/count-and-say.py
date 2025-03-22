class Solution:
    def getCount(self, s:str) -> str:
        l=[]
        l1=[]
        c=s[0]
        l.append(s[0])
        l1.append("1"+s[0])
        cnt=1
        for i in range(1,len(s)):        
            if s[i] in l and s[i]==l[len(l)-1]:
                cnt+=1               
                l1.pop(len(l1)-1)        
                l1.append(str(cnt)+s[i])
            else:        
                l.append(s[i])
                cnt=1       
                l1.append(str(cnt)+s[i])
        s="".join(x for x in l1)        
        return s
    def countAndSay(self, n: int) -> str:
        l=["1","11"]
        s=""
        dd={}
        if n <3:            
            return l[n-1]
        else:
            c=3
            while c<=n:
                print(c,n,l)
                s=self.getCount(l[c-2])
                c+=1
                l.append(s)
                s=""
            return l[n-1]
        