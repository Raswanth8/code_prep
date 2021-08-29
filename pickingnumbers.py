# Hackerrank picking number problem
#Linkedin maxTickets problem
def pickingNumbers(a):
    # Write your code here
    
    a.sort()
    count = 0
    
    for i in range(n):
        for j in range(n):
            if abs(a[j]-a[i]<= 1):
                count = max(count,j-i+1)
    
                
    return count

if __name__ == '__main__':


    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
