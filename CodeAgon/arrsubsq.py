# Minimum Operations to Make a Subsequence

"""
Input: target = [5,1,3], arr = [9,4,2,3,4]
Output: 2
Explanation: You can add 5 and 1 in such a way that makes arr = [5,9,4,1,2,3,4], then target will be a subsequence of arr.

"""
from typing import List
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # len of target - len of LCS
        dp = [[0 for j in range(len(target)+1)] for i in range(len(arr)+1)]
        
        for i in range(len(arr)-1,-1,-1):
            for j in range(len(target)-1,-1,-1):
                if arr[i] == target[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else :
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        
        N = dp[0][0]
        res = 0
        n = len(target)
        res = n - N
        
        return res