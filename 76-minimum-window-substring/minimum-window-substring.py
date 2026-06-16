from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        s1=""
        d=Counter(t)
        

        d1={}
        i=0
        j=0
        while i <= j and j < len(s):
            flag=False
            #print(i,j,d1)
            if s[j] in d.keys():
                if s[j] in d1.keys():
                    d1[s[j]]+=1
                else:
                    d1[s[j]]=1
            j+=1    
            
            
            #print(d,d1,i,j,flag)
            if len(d)==len(d1):
                for k,v in d.items():
                    if k not in d1.keys():
                        flag=False
                        break
                    if v <= d1[k]:             
                        flag=True
                    else:
                        flag=False
                        break
            while flag:   
                #print(flag,i,j,d,d1)  
                #print(s1,i,j,s[i:j],min(s1,s[i:j],key=len))
                if s1=="":
                    s1=s[i:j]
                else:
                    s1=min(s1,(s[i:j]),key=len)
                
                if s[i] in d1.keys():
                    d1[s[i]]-=1
                    if d1[s[i]]==0:
                        del d1[s[i]]
                i+=1
                #print(d,d1,i,j,d.keys()==d1.keys(),l)
                if len(d)==len(d1):               
                    for k,v in d.items():
                        #print(k,v,d1)
                        if k not in d1.keys():
                            flag=False
                            break
                        if v <= d1[k]:             
                            flag=True
                        else:
                            flag=False
                            break
                else:
                    flag=False
                if not flag:
                    #print("flag false")
                    break
                    
            
        return(s1)