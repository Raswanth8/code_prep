# Daily Temperature Problem
"""
Have a monotonic (Decreasing) stack to push and compare elements.
Pop when its a incresing element.
o/p : Difference b/w the 2 indices.

"""
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =  [0] * len(temperatures)
        stack = [] # Stores [temp,index] pair
         
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] =  (i - stackI)
            stack.append([t,i])
        
        return res