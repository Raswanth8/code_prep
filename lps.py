# Longest Palindrome Substring
"""
The approach is to find the centre of the substring and search for palindrome (longest)
We have to handle both odd and even length

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = ""
        lpLen = 0
        
        for i in range(len(s)):
            # odd length
            l,r = i,i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ((r-l+1) > lpLen):
                    lp = s[l:r+1]
                    lpLen = r-l+1
                l -= 1
                r += 1
            
            # even length
            l, r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ((r-l+1) > lpLen):
                    lp = s[l:r+1]
                    lpLen = r-l+1
                l -= 1
                r += 1
            
        return lp
            
        