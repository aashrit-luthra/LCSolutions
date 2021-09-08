class Solution:
    def createParentMapping(self, root, parent, parentMapping):
        if not root:
            return
        parentMapping[root] = parent
        self.createParentMapping(root.left, root, parentMapping)
        self.createParentMapping(root.right, root, parentMapping)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentMapping = {}
        self.createParentMapping(root, None, parentMapping)
        pPointer = p
        qPointer = q
        while pPointer != qPointer:
            if not parentMapping[pPointer]:
                pPointer = q
            else:
                pPointer = parentMapping[pPointer]
            if not parentMapping[qPointer]:
                qPointer = p
            else:
                qPointer = parentMapping[qPointer]
        return pPointer