from collections import deque
class Solution:
    def createMapping(self, root, parent, parentMapping):
        if not root:
            return
        
        parentMapping[root] = parent
        self.createMapping(root.left, root, parentMapping)
        self.createMapping(root.right, root, parentMapping)
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return
        parentMapping = {}
        self.createMapping(root, None, parentMapping)
        nodes = []
        queue = deque()
        seen = set()
        queue.append(target)
        seen.add(target)
        level = -1
        while queue:
            level += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if level == k:
                    nodes.append(node.val)
                elif level < k:
                    if node.left and node.left not in seen:
                        queue.append(node.left)
                        seen.add(node.left)
                    if node.right and node.right not in seen:
                        queue.append(node.right)
                        seen.add(node.right)
                    if parentMapping[node] and parentMapping[node] not in seen:
                        queue.append(parentMapping[node])
                        seen.add(parentMapping[node])
        return nodes