class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=[]
        c=0
        s1=""
        alt = numRows-2

        #print(alt)
        row=0
        col=0
        start=True
        alternate=False

        while c< len(s):
            #edge case
            if numRows==2:
                #print("i am here")
                for i in range(numRows):
                    if c > len(s)-1:
                        l.append((row,col,""))
                    else:                             
                        l.append((row,col,s[c]))  
                    row+=1
                    c+=1
                col+=1
                row=0
                continue
                    
            if start and row < numRows:
                #print("i am here 1 ")
                start = False
                alternate = True
                #print(l,row,col,'sfsfs',start,alternate)
                row=0
                
                for i in range(numRows):   
                    if row >= numRows:
                        row = 0         
                    if c > len(s)-1:
                        l.append((row,col,""))
                    else:                             
                        l.append((row,col,s[c]))  
                        #print("added ",row,col)              
                    row+=1
                    c+=1
                col+=1
                #print(l,row)            
                            
            if alternate and c<len(s):        
                #print("i am here 2")
                alternate=False
                start = True
                row-=1        
                for i in range(alt):
                    row-=1
                    #print(row,"jere",alt)            
                    if c > len(s)-1:
                        l.append((row,col,""))
                    else:             
                        #print(c,len(s))
                        l.append((row,col,s[c]))
                        #print("added2 ",row,col,l)
                    col+=1
                    c+=1
                        
                    
                    
        d={}
        for i in range(len(l)):    
            if l[i][0] in d.keys():
                d[l[i][0]] +=l[i][2]
            else:
                d[l[i][0]]=l[i][2]
        #print(d)

        s="".join(i for i in d.values())
        return s