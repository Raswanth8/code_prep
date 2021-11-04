# All Anagrams in a string Problem
# Use Hash Map to get the count and compare the string
# Sliding Window Approach (l-r, next iteration remove l and l+1, r+1)
# O(n),O(n) - Time complexity, Space Complexity

from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        sCount , pCount = {},{}
        
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i],0) # get is used to handle the case if element is not present. (Avoid Key error)
            sCount[s[i]] = 1 + sCount.get(s[i],0)
            
        res = [0] if sCount == pCount else []
        l = 0
        
        for r in range(len(p),len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r],0)
            sCount[s[l]] -= 1 
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
                
            l +=1
            if sCount == pCount:
                res.append(l)
        return res
        