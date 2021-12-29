# Palindrome Substrings
"""
Similar to Longest Palindrome Substring
Instead of returning the whole string, keep a counter variable to return count.

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            # odd length
            l=r=i
            while l >=0 and r < len(s) and s[l] == s[r]:
                count +=1
                l-=1
                r+=1
                
            # even length
            l,r=i,i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                count +=1
                l-=1
                r+=1
                
        return count