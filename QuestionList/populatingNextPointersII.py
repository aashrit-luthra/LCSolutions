from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            size = len(queue)
            prevNode = None
            for i in range(size):
                currNode = queue.popleft()
                if prevNode:
                    prevNode.next = currNode
                prevNode = currNode
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return root