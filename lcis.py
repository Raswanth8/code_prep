# Longest Continuous Increasing Subsequence
# Brute - force solution
# a[i-1] >=  a[i] -> max(res,temp-i+1)

from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        result = 0
        temp = 0
        
        for i in range(len(nums)):
            if (i > 0 and nums[i-1] >= nums[i]):
                temp = i
            result = max(result,i-temp+1)
                
        return result