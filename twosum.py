def twoSum(nums,target ):
    prevMap ={}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
    return

res = twoSum([1,2,3,6],9)
print(res)