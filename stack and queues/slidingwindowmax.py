# Sliding window maximum 
"""
Monotonic Decreasing queue approach
a = [1,1,1,4]
q = [_,_,_,_,4] popped -(1,1,1)
O(1) * O(n) -> O(n) time complexity

"""
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l,r = 0,0
        
        q = deque()
        while r < len(nums):
            # Pop smaller values and add max to queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # Leftmost most value comparision and popleft
            if l > q[0] :
                q.popleft()
            

            if (r+1) >= k:
                result.append(nums[q[0]]) # append left most values
                l+=1
            r+=1
        
        return result