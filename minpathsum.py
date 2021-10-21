# Minimum Path Sum
# Dynamic Programming approach - O(N^2)

# a[i][j] = grid value + min(a[down],a[right])

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        
        a = [[float("inf")]*(cols+1)for i in range(rows+1)]
        
        a[rows-1][cols] = 0
        
        for r in range((rows)-1,-1,-1):
            for c in range((cols)-1,-1,-1):
                
                a[r][c] =  grid[r][c] + min(a[r+1][c],a[r][c+1])
                
        return a[0][0]
