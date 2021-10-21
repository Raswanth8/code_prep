# Triangle - min path sum (similar)
# Dynamic Programming Approach - O(n^2)

# dp[i] = value + min(dp[i],dp[i]+1) // bottom up

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [0] *( len(triangle) + 1)
        
        for row in triangle[::-1]:
            for i,n in enumerate(row):
                
                dp[i] = n + min(dp[i],dp[i+1])
        return dp[0]
        
                
                
        