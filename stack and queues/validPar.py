# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        if (len(s) % 2 != 0):
            return False
        
        stack  = []
        
        for c in s :
            if (c == '(' or c == '['or c == '{'):
                stack.append(c)
            elif (c == ')' and len(stack) != 0  and stack[-1] == '('):
                stack.pop()
            elif (c == ']' and len(stack) != 0  and stack[-1] == '['):
                stack.pop()
            elif (c == '}' and len(stack) != 0  and stack[-1] == '{'):
                stack.pop()
            else :
                stack.append(c)
                
        return len(stack) == 0