# Remove duplicates from sorted array
# O(n) with no extra memory (2 pointer approach)
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        j = 0 # slow pointer
        
        for i in range(1,len(nums)): # fast pointer
            if nums[i] != nums[j]:
                j+=1
                nums[j] = nums[i]
        return j+1