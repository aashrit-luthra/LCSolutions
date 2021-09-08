class Solution:
    def minHeight(self, nodeVal, nodeMapping, seen):
        # check necessary conditions
        if nodeVal in seen:
            return -1
        if len(set(nodeMapping[nodeVal]) - seen) == 0:
            return 0
        
        # process cell
        seen.add(nodeVal)
        
        # call dfs as needed
        maxH = float('-inf')
        for n in nodeMapping[nodeVal]:
            nMaxH = self.minHeight(n, nodeMapping, seen)
            maxH = max(maxH, nMaxH)
        seen.remove(nodeVal)
        return 1 + maxH
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nodeMapping = {c:[] for c in range(n)}
        for edge in edges:
            nodeMapping[edge[0]].append(edge[1])
            nodeMapping[edge[1]].append(edge[0])
        seen = set()
        minHeight = float('inf')
        minNodes = []
        for i in range(n):
            currMinHeight = self.minHeight(i, nodeMapping, seen)
            if currMinHeight < minHeight:
                minHeight = currMinHeight
                minNodes = [i]
            elif currMinHeight == minHeight:
                minNodes.append(i)
        return minNodes

