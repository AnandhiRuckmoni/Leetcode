class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        flag=True
        open=['(','{','[']
        closed=[')','}',']']
        i=0
        while i < len(s):
            if s[i] in open:
                l.append(s[i])
            if s[i] in closed:
                idx=closed.index(s[i])
                if l == []:
                    flag=False
                    break
                if l[len(l)-1] == open[idx]:
                    l.pop()
                else:
                    flag=False
                    break  
                         
            i+=1
        if flag==True and len(l) != 0:
            flag=False
        
        print(l)
        return flag