class Solution:
    def inBounds(self, matrix, i, j):
        return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowBoundaries = set()
        colBoundaries = set()
        i = 0
        j = 0
        right = True
        left = False
        up = False
        down = False
        output = []
        while True:
            output.append(matrix[i][j])
            if right and self.inBounds(matrix, i, j+1) and j+1 not in colBoundaries:
                j += 1
            elif right and self.inBounds(matrix, i+1, j) and i+1 not in rowBoundaries:
                rowBoundaries.add(i)
                i += 1
                right = False
                down = True
                continue
            elif right:
                break
            
            if down and self.inBounds(matrix, i+1, j) and i+1 not in rowBoundaries:
                i += 1
            elif down and self.inBounds(matrix, i, j-1) and j-1 not in colBoundaries:
                colBoundaries.add(j)
                j -= 1
                down = False
                left = True
                continue
            elif down:
                break
            
            if left and self.inBounds(matrix, i, j-1) and j-1 not in colBoundaries:
                j -= 1
            elif left and self.inBounds(matrix, i-1, j) and i-1 not in rowBoundaries:
                rowBoundaries.add(i)
                i -= 1
                left = False
                up = True
                continue
            elif left:
                break
            
            if up and self.inBounds(matrix, i-1, j) and i-1 not in rowBoundaries:
                i -= 1
            elif up and self.inBounds(matrix, i, j+1) and j+1 not in colBoundaries:
                colBoundaries.add(j)
                j += 1
                up = False
                right = True
                continue
            elif up:
                break
        return output