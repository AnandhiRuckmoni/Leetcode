
class Solution:
    l=[]
    
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def generatesubSets(nums,op,low):
            if low >=len(nums):
                print(op,len(op),sorted(op) in l)
                if sorted(op) not in sorted(l):                    
                    #if not sorted(op) in l:
                        l.append(sorted(op[:]))
                
                return
            
            op.append(nums[low])
            generatesubSets(nums,op,low+1)            
            op.pop()
            generatesubSets(nums,op,low+1)
        generatesubSets(nums,[],0)
        print(l)
        #l.append([])
        return l