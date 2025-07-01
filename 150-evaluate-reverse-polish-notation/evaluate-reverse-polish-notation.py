class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        res=0
        for i in tokens:
            #print(i,int(i).isnumeric())
            
            if i == '+' or i =='-' or i=='*' or i=='/':
                #print(st)
                op1=st.pop()
                op2=st.pop()
                if i == '+':
                    res=int(op2)+int(op1)
                if i =='-':
                    res=int(op2)-int(op1)
                if i == '*':
                    res=int(op2)*int(op1)
                if i=='/':
                    print(op2,op1,int(op2/op1))
                    res=int(op2/op1)
                st.append(res)
            else:
                st.append(int(i))
        while st!=[]:
            res=int(st.pop())
        #print(res)
        return res