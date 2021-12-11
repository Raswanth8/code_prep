# Binary Tree Maximum Path Sum
# DFS  + DP approach

# O(n) compexity

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        dp = [root.val]
        
        def dfs(root):
            
            if not root: 
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax,0) # To neglect negative
            rightMax = max(rightMax,0) # To neglect negative
            
            dp[0] = max(dp[0],root.val + leftMax+rightMax) # Update the result
        
            return root.val + max(leftMax,rightMax) # return the max sum of each node 
        
        dfs(root)
        return dp[0]
        
            
            
            
            
        