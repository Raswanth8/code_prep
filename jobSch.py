# Maximum Profit in Job Scheduling
# O(n^3) 
# @lru_cache for memoization

from typing import List
from functools import lru_cache
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = list(zip(startTime,endTime,profit)) # zip function combine all lists
        jobs.sort()
        
        @lru_cache(None)   
        def func(i):
            if i == N: # base condition
                return 0
            j = i+1
            while(j<N and jobs[i][1]>jobs[j][0]): # next stop
                j +=1
            a = jobs[i][2] + func(j)
            b = func(i+1)
            return max(a,b)
        return func(0)