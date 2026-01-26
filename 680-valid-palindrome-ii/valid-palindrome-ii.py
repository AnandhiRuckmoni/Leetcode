class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        cnt=0
        d={}
        while i <=j and j < len(s):
            if s[i] == s[j]:
                print(i)
                i+=1
                j-=1
            else:
                if len(d.keys()) ==0:
                    d[0]=i
                    d[1]=j
                    i+=1
                    cnt=1
                elif len(d.keys())==2:
                    i=d[0]
                    j=d[1]
                    j-=1
                    cnt=1
                    d[2]=0
                else:
                    cnt=2
                    break
        print(cnt)                    
        if cnt==1 or cnt==0:
            return True
        else:
            return False