class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1
        
        newRoot = TreeNode(root1.val + root2.val)
        newRoot.left = self.mergeTrees(root1.left, root2.left)
        newRoot.right = self.mergeTrees(root1.right, root2.right)
        return newRoot