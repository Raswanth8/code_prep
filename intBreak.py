# Integer Break Problem
# Dynamic Programming approach 
# Rescusive solution could be done using dfs but not effective

"""
n   1 2 3 4
dp  1 2 3 4 (dp should never be less than n, hence we can use the product or the num itself)

"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1} # Base conditon 1 -> 1
        
        for num in range(2,n+1):
            dp[num] = 0 if num == n else num # if condition is to not to break into sub problems 
            for i in range(1,num):
                a = dp[i]*dp[num-i]
                dp[num] = max(dp[num],a)
        return dp[num]