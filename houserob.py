def houserob(arr):
    rob1,rob2 =0,0

# rob1,rob2,i,i+1.....

    for i in arr:
        temp = max(i +rob1,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

result = houserob([1,2,3,1])
print(result)