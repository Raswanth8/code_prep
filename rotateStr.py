# Rotate String Problem
# Also known as Circular Substring.Circular substring means any substring of the rotated source string.
# A shift on moving the leftmost character to the rightmost position.
# O(N+M) Solution

# A+A will contain all substrigs of goal

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if (len(s) != len(goal)):
            return False
        
        if (goal not in s+s):
            return False
        
        return True
        
