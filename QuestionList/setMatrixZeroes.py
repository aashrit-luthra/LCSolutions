class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        fromCol = False
        fromRow = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        fromRow = True
                    if j == 0:
                        fromCol = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        if fromRow:
            for j in range(n):
                matrix[0][j] = 0
        if fromCol:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix
        