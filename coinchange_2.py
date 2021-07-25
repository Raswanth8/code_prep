from typing import List
class Solution:
    def coinchange(self, coins:List[int],amount:int):
        dp = [0]*(amount+1)
        dp[0] = 1

        for c in coins:
            for a in range(1,amount+1):
                if a >= c:
                    dp[a] += dp[a-c]
        return dp[-1]

a = Solution()
b = [1,2,5]
c = 5
a.coinchange(b,c)
print(a.coinchange(b,c))