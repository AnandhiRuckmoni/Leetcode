# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def traverse(self,head,nums):
        l=[]
        l1=[]
        l2=[]
        cnt=0
        curr=head
        while curr:
            l.append(curr.val)
            curr=curr.next
        if sorted(l)==sorted(nums):
            cnt=1
            return cnt
        subcnt=0
        for i in nums:
            l1.append(l.index(i))
        l1.sort()
        cnt=0
        for i in range(len(l1)-1):
            if l1[i+1] - l1[i] == 1:
                subcnt+=1
            else:
                cnt+=1
        print(l1,subcnt,cnt)
        return len(nums)-subcnt
        if subcnt+1 == len(nums):
            l1=[]
            return 1
        print('l1',l1)
        l1=[]
        i=0
        while i < len(l)-1:
            if l[i] in nums and l[i+1] in nums:
                l1.append(l[i])
                l1.append(l[i+1])
                nums.remove(l[i])
                nums.remove(l[i+1])
            i+=1
            if l1!=[]:
                l2.append(l1)
                l1=[]
        
        print(l2,nums,len(l2))
        if nums==[]:
            cnt=len(l2) 
        else:
            cnt=len(l2)+ len(nums)
        return cnt
            
        
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        return self.traverse(head,nums)
        
        