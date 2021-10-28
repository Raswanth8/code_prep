# Edit Distance Problem
# Similar to LCS
# Dynammic Programming approach 
# 2D formation and bottom up

# same element - i+1,j+1 
# insert - i ,j+1 delete - i+1,j replace - i+1,j+1

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[float('inf')] *(len(word2)+1) for i in range(len(word1)+1)]
        
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if(word1[i] == word2[j]):
                    dp[i][j] = dp[i+1][j+1]
                else :
                    dp[i][j] = 1 + min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
        
        return dp[0][0]
                      
        
