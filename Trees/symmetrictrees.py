"""
Symmetric Tree : Left and right subtree should be mirror of each other.
Have a helper function to check whether right and left subtree are mirror and use it main function.
T.C - O(N), S.C - O(logn) 

"""
from typing import  Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.are_symmetric(root.left,root.right)
        
        
    def are_symmetric(self,root1,root2):
        if root1 is None and root2 is None :
            return True
        elif ((root1 is None) != (root2 is None)) or (root1.val != root2.val):
            return False
        else:
            return self.are_symmetric(root1.left,root2.right) and self.are_symmetric(root2.left,root1.right)
