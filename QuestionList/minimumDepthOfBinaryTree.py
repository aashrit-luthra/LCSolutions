#BFS
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)
        level = -1
        while queue:
            level += 1
            levelLength = len(queue)
            for i in range(levelLength):
                node = queue.popleft()
                if not node.left and not node.right:
                    return level + 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return 0

#DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        if root.left:
            return 1 + self.minDepth(root.left)
        if root.right:
            return 1 + self.minDepth(root.right)