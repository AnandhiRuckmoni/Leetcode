class Solution:
    def twoSum(self,nums:list, target: int) -> list:            
        l=[]
        l1=[]
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            l=[]
            complement=target-nums[i];
            if(complement in hashmap and hashmap[complement]!=i):  
                l.append(nums[i])
                l.append(complement)
                l.append(-target)
            if l!=[]:
                if sorted(l) not in l1:
                    l1.append(sorted(l))
        return l1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i=0
        j=len(nums)-1
        visited=[]

        l1=[]

        for i in range(len(nums)):
            l=[]
            if nums[i] not in visited:
                if nums[i]==0:
                    c=0
                else:
                    c=-nums[i]
                l=self.twoSum(nums[i+1:],c)        
                visited.append(nums[i])
                
            if l!=[] and l != None:
                if l not in l1:
                    for item in l:
                        l1.append(item)
                    l=[]
        return l1