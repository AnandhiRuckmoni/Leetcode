class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[]
        l1=[]
        d={}
        s=""
        s1=""
        s2=""
        for i in strs[0]:
            s+=i
            l.append(s)
        print(l)
        s=""
        if len(strs)==1 and len(l) > 0 :
            return max(l)
        for i in range(1,len(strs)):
            l1=[]
            for item in l:
                if strs[i].startswith(item):
                    s+=item+","
            s=s.rstrip(",")
            if s=="":
                s1=""
                return s1
            if len(d)>0:
                print(s)
                if d[0]!=s:
                    print(d[0],s)
                    if "," in d[0]:
                        s2=d[0].split(",")
                    if "," in s:
                        s=s.split(",")
                    for item in s2:
                        if item in s:
                            l1.append(item)
                            print(l1)
                    if len(l1) > 0:
                        d[0]=max(l1)      
                    s2=""
            else:         
                d[0]=s
            s=""            
            print(i,d)
        if len(d)>0:
            if "," in d[0]:
                s=d[0].split(",")
                s1=max(s)
            else:
                s1=d[0]
        return s1