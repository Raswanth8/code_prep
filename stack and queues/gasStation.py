# Gas Station - Circular Tour
# Greedy Problem
"""
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
diff = [-2,-2,-2,3,3]
3 -> 6 -> 4 -> 2 -> 0 (Circular) // Output index : 3
sum(gas) >= sum(cost) , T.C = O(N)

"""
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total <  0 : 
                total = 0
                start = i+1
        return start