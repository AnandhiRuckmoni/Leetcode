# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def comparethetwo(self,main,subtree):
        
        left=None
        right=None
    
        if not main and not subtree:
            return True
        if (main and not subtree) or (not main and subtree):
            return False
        if main.val!=subtree.val:
            return False
        if main.val == subtree.val and (not main.left and not subtree.left) and (not main.right and not subtree.right):
            return True
        
        #print(main.val,subtree.val,main.left,main.right,subtree.left,subtree.right)
        if main.left and subtree.left:
            left=self.comparethetwo(main.left,subtree.left)
        if main.left and not subtree.left:
            left=False
        if not main.left and subtree.left:
            left= False
        if not main.left and not subtree.left:
            left=True
        if main.right and subtree.right:
            right=self.comparethetwo(main.right,subtree.right)
        if main.right and not subtree.right:
            right=False
        if not main.right and subtree.right:
            right= False
        if not main.right and not subtree.right:
            right=True
        
        print(main.val,left,right)
        return left and right
        
    def inorder(self,root):
        l=[]
        if not root:
            return []
        if root.left:
            l+=self.inorder(root.left)
        l.append(root)
        if root.right:
            l+=self.inorder(root.right)
        return l
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """curr=root
        start=None
        start=self.find_node(root,subRoot)
        #print('start',start.val)
        found=False
        print('start',start)
        if start==[]:
            return False
        else:
            for i in start:
                found= self.compare(i,subRoot) 
                if found:
                    break
        return found"""

        l=self.inorder(root)
        x=False
        for i in l:
            print(i.val)
            if i.val==subRoot.val:                
                x=self.comparethetwo(i,subRoot)
                if x:
                    break

        return x
            