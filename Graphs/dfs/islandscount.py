# Number of islands using DFS
from typing import List


class Solution :
    def numIslands(self,grid:List[List[str]])-> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1

                    self.dfs(grid,i,j)
        return count

    def dfs(self,grid,i,j):
        rows = len(grid)
        cols= len(grid[0])

        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != "1":
            return
        
        grid[i][j] = "0"

        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)

a = Solution()

res = a.numIslands( [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(res)

