from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        output = []
        while queue:
            size = len(queue)
            for i in range(size):
                currNode = queue.popleft()
                if i == size-1:
                    output.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return output