class Solution:
    def intToRoman(self, num: int) -> str:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        print(d)
        s=num
        s1=""

        while s > 0:
            startingwith4 = str(s).startswith('4') 
            startingwith9 = str(s).startswith('9')
            if startingwith4:
                l=len(str(s))
                if l == 1:
                    s1+='IV'
                    s-=4
                elif l==2:
                    s1+='XL'
                    s-=40
                elif l==3:
                    s1+='CD'
                    s-=400
            elif startingwith9:
                l=len(str(s))
                if l == 1:
                    s1+='IX'
                    s-=9
                elif l==2:
                    s1+='XC'
                    s-=90
                elif l==3:
                    s1+='CM'
                    s-=900
            else:
                temp = max(j for i,j in d.items() if j <= s)
                s1+="".join(i for i,j in d.items() if j == temp)
                s-=temp
                print(temp,s1)
            
            #s=0
        return(s1)
        