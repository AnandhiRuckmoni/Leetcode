# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_level(self,root,nodeval):
        level=0
        if not root:
            return
        curr=root
        print(curr.val,nodeval)
        if curr.val==nodeval:
            return level
        if nodeval < curr.val:
            
            return 1+self.get_level(curr.left,nodeval)
        if nodeval > curr.val:
            return 1+ self.get_level(curr.right,nodeval)
            
            
        return level

    def getAncestorList(self,root,node,parent):
        l=[]
        if not root:
            return None
        curr=root
        if node.val==curr.val:
            if parent is not None:
                l.append(parent)            
            l.append(node)
            return l
        if node.val < curr.val:
            #print(node.val,curr.val)
            l.append(curr)
            
            if curr.left:
                parent=curr
                
                l+=self.getAncestorList(curr.left,node,parent)
                #print(l)
                
        if node.val > curr.val:
            l.append(curr)
            if curr.right:
                parent=curr
                l+=self.getAncestorList(curr.right,node,parent)
        return l
                
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l1=[]
        l2=[]
        l1=self.getAncestorList(root,p,None)
        l2=self.getAncestorList(root,q,None)
        l=[]
        print(l1,"main", l2)
        if len(l2) > 0 and len(l1) > 0:
            l=[x for x in l1 if x in l2]
        print("main1", l,"common list")
        level=-sys.maxsize
        for i in l:
            x=self.get_level(root,i.val)
            if x > level:
                node=i
                level = x
        if len(l) > 0:
            return node
        else:
            return None