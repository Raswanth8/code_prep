def genParan(n):

    stack =[]
    res =[]

    def backtrack(a,b):
        if a == b == n:
            res.append("".join(stack))
            return
        
        if a < n :
            stack.append("(")
            backtrack(a +1,b)
            stack.pop()
        
        if b < a:
            stack.append(")")
            backtrack(a,b+1)
            stack.pop()
        
    backtrack(0,0)
    return res

c = genParan(3)
print(c)
