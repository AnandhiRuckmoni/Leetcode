# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def roottoleafpath(self,root,s,l):
        if not root:
            return ""
        s=s+str(root.val)+'->'
        if not root.left and not root.right:
            s=s[0:len(s)-2]
            l.append(s)
            return s
        return self.roottoleafpath(root.left,s,l)+self.roottoleafpath(root.right,s,l)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        s=""
        x=self.roottoleafpath(root,s,l)
        return(l)