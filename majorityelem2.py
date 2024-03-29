# Majority Element 2 -> freq > n/3
# Boyer-Moore Approach 
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        cand1,count1 = None,0
        cand2,count2 = None,0
        
        for num in nums:
            if cand1 == num:
                count1+=1
            elif cand2 == num:
                count2+=1
                
            elif count1 == 0:
                cand1 = num
                count1+=1
            elif count2 == 0:
                cand2 = num
                count2+=1
            else :
                count1,count2 == count1 -1 , count2 -1
            
        return [x for x in (cand1,cand2) if nums.count(x) > len(nums)//3]