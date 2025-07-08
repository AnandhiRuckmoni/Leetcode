# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def valid(self,root,low,high):
        curr=root
        if not curr:
            return True
        if curr.val<=low or curr.val>=high:
            return False
        x=self.valid(curr.left,low,curr.val)
        y=self.valid(curr.right,curr.val,high)
        return (x and y)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        x=self.valid(root,-sys.maxsize,sys.maxsize)
        return x