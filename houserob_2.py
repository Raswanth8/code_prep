def rob(arr):
    return max(arr[0],helper(arr[1:]),helper(arr[:-1]))

def helper(arr):
    rob1,rob2 =0,0

# rob1,rob2,i,i+1.....
    for i in arr:
        temp = max(i +rob1,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

result = rob([5,3,1])
print(result)