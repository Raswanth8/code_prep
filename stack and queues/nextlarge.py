# Next Large Element 
"""
nums1 = [4,1,2], nums2 = [1,3,4,2]
Stack : [1]
Hashmap = 1,3
Stack : [3]
Hashmap = 3,4
default : -1

"""
from typing import  List 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        
        for num in nums2:
            while (len(stack)!= 0 and stack[-1]< num): # Take each element in nums2 push in stack and put in hashmap with greater element to 
                # the right
                hashmap[stack.pop()] = num
                
            stack.append(num)
            
        for i in range(len(nums1)):
            nums1[i] = hashmap.get(nums1[i],-1) # Push to nums 1 / default -1
        
        return nums1