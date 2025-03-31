class Solution:
    def myAtoi(self, s: str) -> int:
        s1=""
        s=s.lstrip()
        
        
        
                
        for i in range(len(s)):
            if i ==0 and s[i]=='-':
                if i+1 < len(s) and s[i+1]=="+":
                    s1=""
                else:
                    s1+=s[i]
            elif i ==0 and s[i]=='+':
                continue
            elif s[i].isdigit():
                s1+=s[i]
            elif not s[i].isdigit():
                break
        print(s1)
        try:
            if int(s1) < pow(-2,31):
                s1=str(pow(-2,31))
            if int(s1) > pow(2,31)-1:
                s1=str(pow(2,31)-1)
        except:
            pass
        if s1!="" and s1!="-":
            return int(s1)
        else:
            return 0