class Solution:
    def __init__(self):
        self.maxDiameter = 0
    
    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        self.maxDiameter = max(self.maxDiameter, left + right)
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root)
        return self.maxDiameter