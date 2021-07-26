def maxsum(nums):
    maxSum = nums[0]
    curSum = maxSum

    for i in range(len(nums)):
        curSum = max(nums[i]+curSum,nums[i])
        maxSum = max(curSum,maxSum)

    return maxSum

c = maxsum([-2,2,5,-11,6])
print(c)




