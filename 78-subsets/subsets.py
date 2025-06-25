class Solution:
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def generateSubsets(Input,op, low):
   
            if low == len(Input):
                l.append(op[:])
                return 
            op.append(Input[low])
            generateSubsets(Input,op,low+1)
            op.remove(Input[low])
            generateSubsets(Input,op,low+1)
    
        generateSubsets(nums,[],0)
        return l
    