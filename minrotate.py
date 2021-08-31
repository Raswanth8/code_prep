# Minimum in Rotated Sorted Array O(logn)
# binary search approach

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = (0,len(nums)-1)
        
        while l <=r:
            if nums[l]<=nums[r]:
                res = min(res,nums[l])
                break
            m = l+r // 2
            if nums[m]>= nums[l]:
                l = m + 1
            else :
                r = m - 1
        
        return res
                