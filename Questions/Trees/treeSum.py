# Given a binary tree, find the sum of all nodes

"""

Input: root of binary tree
Process: find the sum of all nodes in the binary tree
- have to visit all nodes
Output: integer (assuming all node's values are integers)

Option:

create a function:

we will use recursion

base case: if node is None/NULL: return 0
- adding 0 makes no difference to the sum

Otherwise, we will return current node's val + leftSubtrees sum + right Subtrees sum (left and right subtree sum
will be found by calling function recursively on them)

"""

def treeSum(root):
    if not root:
        return 0
    return root.val + treeSum(root.left) + treeSum(root.right)