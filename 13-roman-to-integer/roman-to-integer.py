class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1, 'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}
        print(d)
        #s=input()
        print(s)
        i=0
        val=0
        while i < len(s)-1:
            print(i,val)
            if s[i]=='I':
                print(s[i],s[i+1])
                if (s[i+1]=='V'):
                    val+=4
                    i+=2
                elif s[i+1]=='X':
                    val+=9
                    i+=2
                else:
                    val+=d[s[i]]
                    i+=1
            elif s[i]=='X' : 
                print(s[i],s[i+1])
                if (s[i+1]=='L' ) : 
                    val+=40
                    i+=2
                elif s[i+1]=='C':
                    val+=90
                    i+=2
                else:
                    val+=d[s[i]]
                    i+=1
            elif s[i]=='C' : 
                print(s[i],s[i+1])
                if (s[i+1]=='D'):
                    val+=400
                    i+=2
                elif s[i+1]=='M':
                    val+=900
                    i+=2
                else:
                    val+=d[s[i]]
                    i+=1
            else:
                val+=d[s[i]]
                i+=1
        if i == len(s)-1:
            val+=d[s[i]]
        print(val)
        return val