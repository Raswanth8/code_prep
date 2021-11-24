# Burst Ballons 
# Dynamic Programming 
# DFS + caching
# 0(n^3) complexity


from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1]+nums+[1]
        
        dp = {}
        
        def dfs(l,r):
            if l>r: # Out of bounce condition
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = 0
            for i in range(l,r+1): # traverse till end
                coins = nums[l-1]*nums[i]*nums[r+1] # 1*element*1
                coins += dfs(l,i-1)+dfs(i+1,r) # Handling subarray
                dp[(l,r)] = max(dp[(l,r)],coins)
            return dp[(l,r)]
            
        return dfs(1,len(nums)-2) # ignoring the 1s
        