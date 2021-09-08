class Solution:
    def inBounds(self, grid, i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])
    
    def hasValidPathRecursive(self, grid, i, j, seen, directions, fromWhere):
        # check necessary conditions
        if not self.inBounds(grid, i, j) or (i,j) in seen:
            return False
        if not i == 0 or not j == 0:
            if fromWhere == "left" and grid[i][j] not in [1,3,5]:
                print("should be false")
                return False
            if fromWhere == "right" and grid[i][j] not in [1,4,6]:
                return False
            if fromWhere == "up" and grid[i][j] not in [2,5,6]:
                return False
            if fromWhere == "down" and grid[i][j] not in [2,3,4]:
                return False
        if i == len(grid)-1 and j == len(grid[0])-1:
            return True
        
        # process cell
        seen.add((i,j))
        
        # call dfs as needed
        existsPath = False
        print(grid[i][j], directions[grid[i][j]])
        for d in directions[grid[i][j]]:
            fromWhere = ""
            if d[0] > 0:
                fromWhere = "up"
            if d[0] < 0:
                fromWhere = "down"
            if d[1] > 0:
                fromWhere = "left"
            if d[1] < 0:
                fromWhere = "right"
            existsPath = existsPath or self.hasValidPathRecursive(grid, i + d[0], j + d[1], seen, directions, fromWhere)
            if existsPath:
                break
        
        seen.remove((i,j))
        return existsPath
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        seen = set()
        up, down, left, right = [-1,0], [1,0], [0,-1], [0,1]
        directions = {
            1: [left, right],
            2: [up, down],
            3: [left, down],
            4: [right, down],
            5: [left, up],
            6: [right, up]
        }
        return self.hasValidPathRecursive(grid, 0, 0, seen, directions, "")