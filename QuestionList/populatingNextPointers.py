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

class Solution:
    def connectRecursive(self, root1, root2):
        # check necessary conditions
        if not root1 and not root2:
            return
        
        # process cell
        root1.next = root2
        
        # call dfs as needed
        self.connectRecursive(root1.left, root1.right)
        self.connectRecursive(root2.left, root2.right)
        self.connectRecursive(root1.right, root2.left)
        
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        self.connectRecursive(root.left, root.right)
        return root