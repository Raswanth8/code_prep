# Target Sum Problem 
# Dynamic Programming Approach
# O(n+t) complexity

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index,total) -> number of ways
        
        def backtrack(i,t):
            
            if i == len(nums): # Base case 1
                return 1 if t == target else 0
            if (i,t) in dp: # Base Case 2
                return dp[(i,t)]
            
            dp[(i,t)] = (backtrack(i+1,t+nums[i])+backtrack(i+1,t-nums[i]))
            
            return dp[(i,t)]
        return backtrack(0,0)
        