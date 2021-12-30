# Longest Valid Parentheses

"""
Similar to valid parentheses problem, but append index to the stack instead of brackets.
O(N),O(N) -Time, Space Complexity.

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1] # To handle edge cases like "((())"
        res = 0
        
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            else :
                stack.pop()
                if not stack:
                    stack.append(i) # Next index
                else:
                    res = max(res,i-stack[-1]) 
        
        return res
        