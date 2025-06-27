# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addtofront(self,head,curr):
        if not head:
            return
        #print('fn',curr.val,head.val,curr.next,head.next)
        curr.next=head
        head=curr
        return head
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=[]
        c=None
        firstnodelink=None
        if not head:
            return None
        curr=head
        index=1
        while index<= left-1:
            index+=1
            firstnodelink=curr
            print(firstnodelink.val)
            curr=curr.next
        curr=head
        index=1
        while curr:
            if index>=left and index <= right:
                l.append(curr)
            curr=curr.next
            index+=1
        if l==[] or len(l)==1:
            return head
        if l!=[]:
            print(l)
            lastnodelink=l[len(l)-1]
            print(lastnodelink.val,"c")
            if lastnodelink.next:
                c=lastnodelink.next
            #swap the first 2 nodes
            if len(l)>=2:
                t=l[1].next
                l[1].next=l[0]
                l[0].next=c
                newhead=l[1]

                for i in range(2,len(l)):
                    #print(i)                
                    newhead=self.addtofront(newhead,l[i])
            print(c,'rp',firstnodelink)
            if not firstnodelink and not c:
                head=l[len(l)-1]
                return head
            
            if not firstnodelink and c:
                l[0].next=c
                head=l[len(l)-1]
                return head
                #return newhead
            if firstnodelink and not c:
                firstnodelink.next=l[len(l)-1]
                return head
            
            if firstnodelink and c:
                print('jere',firstnodelink.val,c.val)
                firstnodelink.next=l[len(l)-1]
                l[0].next=c

                return head