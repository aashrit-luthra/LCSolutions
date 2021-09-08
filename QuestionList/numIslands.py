class Solution:
    def inBounds(self, i, j, grid):
        return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
    
    def dfs(self, i, j, grid):
        # check nessessary conditions
        if not self.inBounds(i, j, grid) or grid[i][j] == "0":
            return
        
        # process cell
        grid[i][j] = "0"
        
        # call dfs as needed
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for d in directions:
            self.dfs(i+d[0],j+d[1],grid)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    numIslands += 1
                    self.dfs(i, j, grid)
        return numIslands