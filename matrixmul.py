import sys
def matrixMul(mat):
    n = len(mat)
    c = [[0 for x in range(n+1)] for y in range(n+1)]
    
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j = i+l-1
            c[i][j] = sys.maxsize
            
            k = i
            while(j<n and k<= j-1):
                cost = c[i][k] + c[k + 1][j] + mat[i - 1] * mat[k] * mat[j] # dp formula
                
                if cost < c[i][j]:
                    c[i][j] = cost
                k = k+1
    return c[1][n-1]

mat = [10, 30, 5, 60]
print('The minimum cost is', matrixMul(mat))