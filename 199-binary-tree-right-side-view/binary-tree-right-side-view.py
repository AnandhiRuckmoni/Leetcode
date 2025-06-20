# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        left=[]
        right=[]
        if not root:
            return []
        left+=self.rightSideView(root.left)
        right+=self.rightSideView(root.right)
        
        if left==[] and right ==[]:
            l+=[root.val]
            return l
        if len(right)>=len(left):
            l+=[root.val]+right
            return l
        if len(right)<len(left):            
            x=len(left)-len(right)
            #l+=left[0:x]+right+[root.val]
            y=left[::-1]
            l+=[root.val]+right+y[0:x][::-1]
            print(left[::-1],right,root.val)
            return l
    