# Majority Element -> freq > n/2
# Boyer-Moore Approach 
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj_cand = None
        
        for num in nums:
            if count == 0:
                maj_cand = num
            if num == maj_cand:
                count+=1
            else:
                count-=1
                
        return maj_cand
                

        