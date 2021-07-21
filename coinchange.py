from typing import List

class Solution:
    def coinchange(self, coins:List[int],amount:int):
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a - c >=0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        
        return dp[amount] if dp[amount]!= amount + 1 else -1

a = Solution()
b = [1,3,4,5]
c = 7
a.coinchange(b,c)
print(a.coinchange(b,c))