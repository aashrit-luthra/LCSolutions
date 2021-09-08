from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        finalOutput = []
        reverseState = False
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverseState:
                level.reverse()
            reverseState = not reverseState
            finalOutput.append(level)
        return finalOutput