class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        leftTree = root.left
        root.left = root.right
        root.right = leftTree
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root