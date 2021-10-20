# Longest increasing sequence
# Dynamic Programming Approach - O(n^2)

# dp[0] = max(1,1+ dp[1],1+dp[2])

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
                    
        return max(dp)

