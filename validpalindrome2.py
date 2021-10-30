# Valid Palindrome II Problem
# Two pointer approach
# O(n) Time Complexity and O(1) space complexity
# Create a function with same logic to check substring

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        
        while l<=r:
            if s[l] != s[r]:
                return self.checkSub(s,l+1,r) or self.checkSub(s,l,r-1)
            l,r = l+1,r-1
        return True
        
    def checkSub(self,s,i,j):
        l,r = i,j
        
        while l<=r:
            if s[l] != s[r]:
                return False
            l,r = l+1,r-1
        return True
        

