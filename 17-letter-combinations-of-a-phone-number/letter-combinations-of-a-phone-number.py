class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={"2":"abc", "3":"def", "4":"ghi","5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"}

        l=[]
        l1=[]
                
        s=[]
        if digits=="":
            return (l)
        for i in d[digits[0]]:
            s.append(i)
        if len(digits)==1:
            l1=s

        for i in range(1,len(digits)):    
            s2=d[digits[i]]
            print(s2)    
            for j in range(len(s)):        
                #print(s[j])
                for x in s2:
                    l.append(s[j]+x)  
                    #print(l)         
            print("here")    
            s=l

        for i in l:
            if len(i) == len(digits):
                print(i)
                l1.append(i)
        return l1