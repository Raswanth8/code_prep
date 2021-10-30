# Valid Anagram Problem
# O(n),O(n) - Time complexity, Space Complexity
# Using Hash map to get count of each character and check with the other string

# return sorted(s) == sorted(t) 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        countS,countT = {},{}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) # get is used to handle the case if element is not present. (Avoid Key error)
            countT[t[i]] = 1 + countT.get(t[i],0)
            
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True
        
        