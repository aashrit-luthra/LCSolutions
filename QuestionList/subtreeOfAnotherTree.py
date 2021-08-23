class Solution:
    def isEqual(self, root1, root2):
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1):
            return False
        return root1.val == root2.val and self.isEqual(root1.left, root2.left) and self.isEqual(root1.right, root2.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return self.isEqual(root, subRoot)
        return self.isEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)