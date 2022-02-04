# Backspace String Compare
"""
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Use stack and define a helper function and check for equality.

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def convert(word):
            stack = []
            for c in word:
                if c  == '#':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        
        return convert(s) ==  convert(t)
        