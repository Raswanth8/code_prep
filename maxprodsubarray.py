def maxprod(nums):
    result = max(nums)
    curMax,curMin = 1,1

    for i in nums:
        curMax = max(i*curMax,i*curMin,i)
        curMin = min(i*curMax,i*curMin,i)

        result = max(result,curMax)
    
    return result

c = maxprod([2,3,-2,4])
print(c)