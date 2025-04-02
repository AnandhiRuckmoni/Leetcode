class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        s=""
        for i in digits:
            s+=str(i)

        c=int(s)
        c+=1
        s=str(c)
        for i in s:
            l.append(int(i))
        return l