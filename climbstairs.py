def climbstairs(n):
    one,two = 1,1

    for i in range(0,n-1):
        temp = one
        one = one + two
        two = temp

    return one

a = climbstairs(10)

print(a)