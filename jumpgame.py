
def jumpgame(arr):
    goal = len(arr) -1

    for i in range(len(arr)-1,-1,-1):
        if i + arr[i] >= goal:
            goal = i
    
    return True if goal == 0 else False

res = jumpgame([3,2,1,0,4])
print(res)