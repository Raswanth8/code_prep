# Search Insert position
# O(logn) time

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = (0,len(nums)-1)
        
        while l<=r:
            m = (l+r) // 2
            
            if nums[m] == target:
                return m
            
            if target> nums[m]:
                l = m+1
            else:
                r = m-1     
        return l