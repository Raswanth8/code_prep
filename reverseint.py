class Solution:
    def reverse(self, x: int) -> int:
        
        rev = int(str(abs(x))[::-1])
        
        if x < 0:
            rev = - rev
    
        return rev * ( -2**31 <= rev <= 2**31-1 )
        