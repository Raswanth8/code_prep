# Longest Palindrome Subsequense
"""
Similar to LCS Problems
Dynammic Programming approach 
2D matirx formation and bottom up 
One small diff from LCS is that move i+1 and j-1

"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        
        for i in range(len(s)-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 +dp[i+1][j-1]
                    
                else :
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
                
        