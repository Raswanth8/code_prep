def maxAlternatingsum(nums):
    evenSum,oddSum = 0,0

    for i in range(len(nums)-1,-1,-1):
        a = max(oddSum + nums[i],evenSum)
        b = max(evenSum - nums[i],oddSum)

        evenSum,oddSum = a,b

    return evenSum

c = maxAlternatingsum([4,2,5,3])
print(c)
