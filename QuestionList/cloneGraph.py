class Solution:
    def cloneGraphRecursive(self, node, newNode, seen):
        seen[newNode.val] = newNode
        for n in node.neighbors:
            isNeighborAlready = False
            for i in range(len(newNode.neighbors)):
                if n.val == newNode.neighbors[i].val:
                    isNeighborAlready = True
                    break
            if not isNeighborAlready:
                newNeighbor = Node(0)
                if n.val in seen:
                    newNeighbor = seen[n.val]
                    newNode.neighbors.append(newNeighbor)
                    newNeighbor.neighbors.append(newNode)
                else:
                    newNeighbor = Node(n.val)
                    newNode.neighbors.append(newNeighbor)
                    newNeighbor.neighbors.append(newNode)
                    self.cloneGraphRecursive(n, newNeighbor, seen)
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        newNode = Node(node.val)
        seen = {}
        self.cloneGraphRecursive(node, newNode, seen)
        return newNode