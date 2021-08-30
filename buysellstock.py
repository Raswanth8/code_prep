# Buy and sell stock problem O(n)
# left - buy right - sell

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r = 0,1
        maxP = 0
        
        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit,maxP)
            else:
                l = r
            r+=1
        return maxP