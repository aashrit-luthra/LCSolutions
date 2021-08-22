class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        newTarget = targetSum - root.val
        if not root.left and not root.right and not newTarget:
            return True
        if not root.left and not root.right:
            return False
        if not root.left:
            return self.hasPathSum(root.right, newTarget)
        if not root.right:
            return self.hasPathSum(root.left, newTarget)
        return self.hasPathSum(root.left, newTarget) or self.hasPathSum(root.right, newTarget)