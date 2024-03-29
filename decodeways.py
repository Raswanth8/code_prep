def decodeways(s):
    dp = {len(s) : 1}

    for i in range(len(s)-1,-1,-1):
        if s[i] == '0':
            return 0
        else :
            dp[i] = dp[i+1]
        
        if(i+1 <len(s) and (s[i] == '1' or s[i] == '2' and s[i+2] in '0123456')):
            dp[i] +=dp[i+2]

    return dp[0]

res = decodeways("12")
print(res)