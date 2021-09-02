class Solution:
    def inBounds(self, pos, board):
        return pos[0] >= 0 and pos[0] < len(board) and pos[1] >= 0 and pos[1] < len(board[0])
    
    def existsRecursive(self, board, word, idx, i, j, visited):
        if idx == len(word):
            return True
        if not self.inBounds((i,j), board) or board[i][j] != word[idx] or (i,j) in visited:
            return False
        visited.add((i,j))
        if self.existsRecursive(board, word, idx + 1, i + 1, j, visited) or self.existsRecursive(board, word, idx + 1, i - 1, j, visited) or self.existsRecursive(board, word, idx + 1, i, j + 1, visited) or self.existsRecursive(board, word, idx + 1, i, j - 1, visited):
            return True
        visited.remove((i,j))
        return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and (i,j) not in visited:
                    if self.existsRecursive(board, word, 0, i, j, visited):
                        return True
        return False